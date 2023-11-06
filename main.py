import json
from datetime import datetime

def mask_card_number(card_number):
    # Разбиваем номер карты на блоки по 4 цифры
    blocks = [card_number[i:i+4] for i in range(0, len(card_number), 4)]
    # Маскируем все блоки, кроме первого и последнего
    masked_blocks = ['XXXX'] + [block[-2:] for block in blocks[1:-1]] + ['XXXX']
    # Соединяем блоки с пробелами
    masked_number = ' '.join(masked_blocks)
    return masked_number

def mask_account_number(account_number):
    # Оставляем только последние 4 цифры номера счета
    masked_number = '**' + account_number[-4:]
    return masked_number

def print_last_operations(json_string):
    data = json.loads(json_string)
    operations = data

    # Сортировка операций по дате прибытия или создания в порядке убывания
    operations.sort(key=lambda x: x.get('date') or x.get('arrivedAt') or x.get('createdAt') or '', reverse=True)

    # Вывод информации о последних 5 операциях
    for i, operation in enumerate(operations[:5]):
        date_str = operation.get('date') or operation.get('arrivedAt') or operation.get('createdAt')

        # Исключение операций без времени
        if not date_str:
            continue

        # Преобразование строки в объект datetime
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')

        description = operation['description']
        source = mask_account_number(operation.get('from', ''))
        destination = mask_account_number(operation['to'])
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        # Маскирование номера карты
        if 'card' in operation:
            card_number = operation['card']['number']
            masked_card_number = mask_card_number(card_number)
        else:
            masked_card_number = ''

        print(f"Дата: {date.strftime('%d.%m.%Y')}")
        print(f"Описание: {description}")
        print(f"Источник: {source}")
        print(f"Назначение: {destination}")
        print(f"Сумма: {amount} {currency}")
        # Вывод замаскированного номера карты
        if masked_card_number:
            print(f"Номер карты: {masked_card_number}")
        print()

        if i != len(operations[:5]) - 1:
            print()

# Чтение содержимого файла operations.json
with open('operations.json') as file:
    json_string = file.read()

print_last_operations(json_string)







