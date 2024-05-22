class ATM:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def create_user(self, username, pin):
        if username in self.users:
            print("User already exists.")
            return False
        self.users[username] = {'pin': pin, 'balance': 0, 'transactions': []}
        print(f"User {username} created successfully.")
        return True

    def authenticate_user(self, username, pin):
        user = self.users.get(username)
        if user and user['pin'] == pin:
            self.logged_in_user = username
            print(f"User {username} logged in successfully.")
            return True
        else:
            print("Authentication failed. Please check your username and pin.")
            return False

    def logout(self):
        self.logged_in_user = None
        print("User logged out successfully.")

    def check_balance(self):
        if self.logged_in_user:
            balance = self.users[self.logged_in_user]['balance']
            print(f"Current balance: ${balance}")
            return balance
        else:
            print("No user is logged in.")
            return None

    def deposit(self, amount):
        if self.logged_in_user and amount > 0:
            self.users[self.logged_in_user]['balance'] += amount
            self.users[self.logged_in_user]['transactions'].append(f"Deposited ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit failed. Please check the amount and login status.")

    def withdraw(self, amount):
        if self.logged_in_user and amount > 0:
            balance = self.users[self.logged_in_user]['balance']
            if balance >= amount:
                self.users[self.logged_in_user]['balance'] -= amount
                self.users[self.logged_in_user]['transactions'].append(f"Withdrew ${amount}")
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal failed. Please check the amount and login status.")

    def transaction_history(self):
        if self.logged_in_user:
            transactions = self.users[self.logged_in_user]['transactions']
            if transactions:
                print("Transaction history:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found.")
        else:
            print("No user is logged in.")

# Simulation
atm = ATM()
atm.create_user("john_doe", "1234")
# atm.authenticate_user("john_doe", "1234")
# atm.check_balance()
# atm.deposit(1000)
# atm.check_balance()
# atm.withdraw(500)
# atm.check_balance()
# atm.transaction_history()
# atm.logout()
