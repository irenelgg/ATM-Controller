import unittest
from atm_controller import ATMController 

class TestATMController(unittest.TestCase):
    def setUp(self):
        self.atm = ATMController()

    def test_insert_card_valid_account(self):
        result = self.atm.insert_card("123456")
        self.assertTrue(result)
        self.assertEqual(self.atm.cur_accounts, "123456")

    def test_insert_card_invalid_account(self):
        result = self.atm.insert_card("999999")
        self.assertFalse(result)
        self.assertIsNone(self.atm.cur_accounts)

    def test_validate_correct_pin(self):
        self.atm.insert_card("123456")
        result = self.atm.validate_pin(1234)
        self.assertTrue(result)

    def test_validate_incorrect_pin(self):
        self.atm.insert_card("123456")
        result = self.atm.validate_pin(1111)
        self.assertFalse(result)

    def test_see_balance(self):
        self.atm.insert_card("123456")
        self.atm.validate_pin(1234)
        balance = self.atm.see_balance()
        self.assertEqual(balance, 1000)

    def test_deposit_valid_amount(self):
        self.atm.insert_card("123456")
        self.atm.validate_pin(1234)
        new_balance = self.atm.deposit(200)
        self.assertEqual(new_balance, 1200)

    def test_deposit_invalid_amount(self):
        self.atm.insert_card("123456")
        self.atm.validate_pin(1234)
        new_balance = self.atm.deposit(-50)
        self.assertIsNone(new_balance)

    def test_withdraw_valid_amount(self):
        self.atm.insert_card("123456")
        self.atm.validate_pin(1234)
        new_balance = self.atm.withdraw(500)
        self.assertEqual(new_balance, 500)

    def test_withdraw_invalid_amount(self):
        self.atm.insert_card("123456")
        self.atm.validate_pin(1234)
        new_balance = self.atm.withdraw(1500)  # Exceeds balance
        self.assertIsNone(new_balance)

    def test_withdraw_negative_amount(self):
        self.atm.insert_card("123456")
        self.atm.validate_pin(1234)
        new_balance = self.atm.withdraw(-100)  # Invalid amount
        self.assertIsNone(new_balance)

    def test_withdraw_no_card_inserted(self):
        new_balance = self.atm.withdraw(100)
        self.assertIsNone(new_balance)

if __name__ == "__main__":
    unittest.main()
