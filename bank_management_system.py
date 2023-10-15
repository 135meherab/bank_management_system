import random

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.user_accounts = []
        self.admin_account = None
        self.total_bank_balance = 0
        self.total_loan = 0
    def add_user_account(self, account):
        self.user_accounts.append(account)

    def set_admin_account(self, account):
        self.admin_account= account

    def check_bank_balance(self):
        print(self.total_bank_balance)

    def check_total_loan(self):
        print(self.total_loan)    

    def see_all_user(self):
        for account in self.user_accounts:
            print(f"Name: {account.name} ---> accountNo: {account.ac_no} ---> balance: {account.balance}")
    
    def account_delete(self, name, email):
        for account in self.user_accounts:
            if account.name == name and account.email == email:
                self.user_accounts.remove(account)
                print('account removed successfully')
    def band_form_taking_loan(self, name, email, switch):
        for account in self.user_accounts:
            if account.name == name and account.email == email:
                if switch =='off':
                    account.is_loan_acitve = False
                else:
                    account.is_loan_acitve = False



class UserAccount:
    def __init__(self, name, email, password, address, ac_type) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.ac_type = ac_type
        self.balance = 0
        self.loan_amount = 0
        self.ac_no ='2023'+ name + str(random.randint(999,10001))
        self.transactions = {}
        self.number_of_loan = 0
        self.is_loan_acitve = True

    def check_balance(self):
        print(f'Your Current balance is: {self.balance}')

    def deposite(self, amount):
        self.balance += amount
        self.transactions['deposite'] = amount

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f'{amount} successfully withdrawed.')
                print(f"Your new balance: {self.balance}")
                self.transactions['withdraw'] = amount
            else:
                print("Withdrawal amount exceeded")
        else:
            print("Invalid amount")

    def take_loan(self, amount):
        if self.is_loan_acitve:
            self.number_of_loan += 1
            if self.number_of_loan < 3:
                self.loan_amount += amount
                self.balance += amount
                self.transactions[f'loan{self.number_of_loan}'] = amount
                print(f'You have successfully taken a loan of {amount}')
                print(f'your current balacne is : {self.balance}')
            else:
                print("you reached to your maximum cepacity of taking loan")
        else:
            print('Admin has band you from taking loan')
class AdminAccount(Bank):
    def __init__(self, name, email, password) -> None:
        super().__init__(name)
        self.email = email
        self.password = password



def main():
    ibl = Bank('Islami Bank Limited')
    admin = ['admin', 'admin@ibl.com', 'admin']
    ibl.set_admin_account(admin)
    current_user = None
    while True:
        if current_user == None:
            choice = input('Login or Register (L/R): ')
            if choice == 'R':
                name = input("Enter Your name: ")
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                address = input("Enter Your address: ")
                ac_type = input("Savings or Current: ")
                ac = UserAccount(name, email, password, address, ac_type)
                ibl.add_user_account(ac)
                current_user = ac
            elif choice =='L':
                email = input("Enter Your email: ")
                password = input("Enter your password: ")
                op = input("admin or user (a/u): ")
                if op == 'u':
                    for account in ibl.user_accounts:
                        if account.email == email:
                            if account.password == password:
                                current_user = account
                                break
                            else:
                                print('Wrong password')
                elif op == 'a':
                        if ibl.admin_account[1] == email:
                            if ibl.admin_account[2] == password:
                                current_user = ibl.admin_account
                            else:
                                print('Wrong password')
                        else:
                            print('Wrong email')
                else:
                    print('Wrong key')

            else:
                print('Wrong key')
        else:
            if current_user in ibl.user_accounts:
                print(f'----------WellCome {current_user.name}------------')
                print('1. Check Balance')
                print('2. Deposite amount')
                print('3. Withdraw amount')
                print('4. Cheack Transactions')
                print('5. Take a loan')
                print('6. Transfar amount')
                print('7. Logout')
                op = input("Enter your option: ")
                if op == '1':
                    current_user.check_balance()
                elif op == '2':
                    amount = int(input('Enter Amount: '))
                    current_user.deposite(amount)
                    ibl.total_bank_balance += amount
                elif op == '3':
                    if current_user.balance > 0:
                        amount = int(input('Enter Amount: '))
                        if amount <= current_user.balance:
                            if amount <= ibl.total_bank_balance:
                                current_user.withdraw(amount)
                                ibl.total_bank_balance -= amount
                            else:
                                print('the bank is bankrupt')
                        else:
                            print('Withdrawal amount exceeded')
                    else:
                        print('pleace deposite first or take a loan')
                elif op == '4':
                    for key, value in current_user.transactions.items():
                        print(f'{key} ---> {value}')    
                elif op == '5':
                    amount = int(input('Enter Amount: '))
                    if amount <= ibl.total_bank_balance:
                        current_user.take_loan(amount)
                        ibl.total_loan += amount
                        ibl.total_bank_balance -= amount
                    else:
                        print('the bank is bankrupt')
                elif op == '6':
                    name = input("Enter another user name: ")
                    email = input("Enter another user email: ")
                    another_user = None
                    another_user_found = False
                    for account in ibl.user_accounts:
                        if account.name == name and account.email == email:
                            another_user = account
                            another_user_found = True
                            break
                    if another_user_found:
                        amount = int(input("Enter amount: "))
                        if amount > 0:
                            if amount <= current_user.balance:
                                current_user.balance -= amount
                                another_user.balance += amount
                                another_user.transactions[f'transfar from {current_user.name}'] = amount
                                current_user.transactions[f'transfar to {another_user.name}'] = amount
                                print("successfully transfared")
                            else:
                                print('you do not have enough balance')
                        else:
                            print('invalid amount')
                    else:
                        print('Account does not exist')
                elif op == '7':
                    current_user = None
                else:
                    print('Wrong key')
                
            elif current_user == ibl.admin_account:
                print(f'****____WellCome Admin____****')
                print('1. creat account')
                print('2. Delete account')
                print('3. See all user account')
                print('4. Check bank total balance')
                print('5. chack total loan amount')
                print('6. Turn on/off loan feature')
                print('7. Logout')

                op = input("Enter your option: ")
                if op == '1':
                    name = input("Enter Your name: ")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    address = input("Enter Your address: ")
                    ac_type = input("Savings or Current: ")
                    ac = UserAccount(name, email, password, address, ac_type)
                    ibl.add_user_account(ac)
                elif op == '2':
                    name = input("Enter account Name: ")
                    email = input("Enter account Email: ")
                    ibl.account_delete(name,email)
                elif op =='3':
                    ibl.see_all_user()
                elif op == '4':
                    ibl.check_bank_balance()
                elif op == '5':
                    ibl.check_total_loan()
                elif op == '6':
                    name = input("Enter Your name: ")
                    email = input("Enter your email: ")
                    switch = input("Turn on/off: ")
                    ibl.band_form_taking_loan(name, email,switch)
                elif op == '7':
                    current_user = None
                else:
                    print('wrong key')
            else:
                print('Acccount does not exist')        

if __name__ == '__main__':
    main()