def convert_to_uppercase(string):
    #changing strings to uppercase
    #argument str to convert
    #returns str converted to uppercase
    return string.upper()

def capitalize_fist_letters(string):
    #capitalizes first letter
    #arguments: string(str): string to capitalize

    #returns: str: string with first letter

    words=string.split()
    capitalized_words=[word.capitalize() for word in words]
    return ''.join(capitalized_words)
