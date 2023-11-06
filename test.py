import unittest
from main import mask_card_number, mask_account_number


class TestCardNumberMasking(unittest.TestCase):

    def test_mask_card_number(self):
        card_number = "1234567812345678"
        masked_number = mask_card_number(card_number)
        self.assertEqual(masked_number, "XXXX 78 34 XXXX")

    def test_mask_account_number(self):
        account_number = "1234567890"
        masked_number = mask_account_number(account_number)
        self.assertEqual(masked_number, "**7890")






