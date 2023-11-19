import unittest
from main import mask_card_number, mask_account_number, extract_non_digits

class ExtractTestCase(unittest.TestCase):

    def test_extract_non_digits(self):
        card_number = '4111-1111-1111-1111'
        expected_non_digits = '---'
        non_digits = extract_non_digits(card_number)
        self.assertEqual(non_digits, expected_non_digits)

class MaskTestCase(unittest.TestCase):

    def test_mask_card_number(self):
        card_number = '4111 1111 1111 1111'
        masked_number = mask_card_number(card_number)
        expected_masked_number = '4111 11** **** 1111'
        self.assertEqual(masked_number, expected_masked_number)

    def test_mask_account_number(self):
        account_number = '1234567890'
        masked_number = mask_account_number(account_number)
        expected_masked_number = '**7890'
        self.assertEqual(masked_number, expected_masked_number)

if __name__ == '__main__':
    unittest.main()
