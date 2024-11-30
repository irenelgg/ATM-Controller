# ATM Controller

A Python implementation of a simple ATM controller that manages user interactions such as card insertion, PIN validation, balance inquiries, deposits, and withdrawals.

## Features
- **Insert Card**: Validates the account number.
- **PIN Validation**: Authenticates the user with a PIN.
- **View Balance**: Displays the current account balance.
- **Deposit**: Allows users to deposit money into their account.
- **Withdraw**: Allows users to withdraw money, ensuring sufficient funds are available.

## Requirements
- Python 3.12.4 or higher

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/irenelgg/ATMController.git
   cd ATMController
2. Ensure Python is installed:
   ```bash
   python3 --version
## Usage
Running the ATM Controller
1. Save the ATMController class implementation in a file named atm_controller.py.
2. Run the script directly to simulate an ATM session:
   ```bash
   python3 atm_controller.py
## Running Tests
1. Save the test cases in a file named test.py.
2. Run the tests using unittest:
   ```bash
   python3 -m unittest test.py
## Project Structure
```
ATMController/
├── atm_controller.py  # Main ATMController class implementation
├── test.py            # Test cases for the ATMController
├── README.md          # Project documentation
```

## Methods Overview

The `ATMController` class includes the following methods:

- `insert_card(account_number)` validates the account number and returns `True` for valid accounts or `"Invalid account number."` for invalid accounts.
- `validate_pin(pin)` checks the PIN for the current account. Returns `True` for correct PIN or `False` otherwise.
- `see_balance()` displays the current account balance.
- `deposit(amount)` adds funds to the account. Returns the new balance for valid amounts or `None` for invalid deposits.
- `withdraw(amount)` deducts funds from the account. Returns the new balance for valid amounts or `None` for insufficient funds or invalid requests.
