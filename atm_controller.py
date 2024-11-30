class ATMController:
     def __init__(self):
          self.accounts = {
               # Key: Account Number, Value: {Pin, Balance}
               "123456": {"pin": 1234, "balance": 1000},
               "654321": {"pin": 4321, "balance": 500}
          }
          self.cur_accounts = None
          
     def insert_card(self, account_number):
          if account_number in self.accounts:
               self.cur_accounts = account_number
               print(f"Card accepted for account # {account_number}.")
               return True
          else:
               print("Invalid account number.")
               return False
     
     def validate_pin(self, pin):
          if self.cur_accounts is None:
               print("No card inserted.")
               return False
          if self.accounts[self.cur_accounts]["pin"] == pin:
               print("PIN validated")
               return True
          else:
               print("Incorrect PIN.")
               return False
     
     def select_account(self):
          if self.cur_accounts:
               print(f"Account {self.cur_accounts} selected.")
               return True
          print("No account selected.")
          return False
     
     def see_balance(self):
          if self.cur_accounts:
               balance = self.accounts[self.cur_accounts]["balance"]
               print(f"Current balance: ${balance}")
               return balance
          else:
               print("No account selected.")
               return None
     
     def deposit(self, amount):
          if self.cur_accounts:
               if amount > 0:
                    self.accounts[self.cur_accounts]["balance"] += amount
                    print(f"${amount} deposited. New balance: {self.accounts[self.cur_accounts]["balance"]}")
                    return self.accounts[self.cur_accounts]["balance"]
               else:
                    print("Invalid deposit amount.")
                    return None
          print("No account selected.")
          return None
     
     def withdraw(self, amount):
          if self.cur_accounts:
               if 0 < amount <= self.accounts[self.cur_accounts]["balance"]:
                    self.accounts[self.cur_accounts]["balance"] -= amount
                    print(f"${amount} withdrawn. New balance: {self.accounts[self.cur_accounts]["balance"]}")
                    return self.accounts[self.cur_accounts]["balance"]
               else:
                    print("Invalid withdrawal amount.")
                    return None
          print("No account selected.")
          return None