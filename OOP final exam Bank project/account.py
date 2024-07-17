from datetime import datetime
class Account:
    def __init__(self,User,Bank) -> None:
        self.user=User
        self.__balance=0
        self.__transaction=[]
        self.loan_count=1
        self.flag_loan=True
        self.account_number=0
        self.bank=Bank
        self.loan=0

    def deposit(self,amount):
        if amount<0:
            print("Invalid deposit....")
        else:
            self.__balance+=amount
            self.__transaction.append((datetime.now(),f"deposit amount is {amount}"))
            print("....deposit is success....")

    def withdraw(self,amount):
        if amount < 0 or amount>self.__balance:
            print("Withdrawal amount exceeded")
        else:
            self.__balance-=amount
            self.__transaction.append((datetime.now(),f"withdraw amount is {amount}"))
            print("....withdraw is success....")

    def available_balance(self):
        print(f"the available balance of {self.user.name} is {self.__balance} ")
        return self.__balance

    def transaction_history(self):
        print(f"the owner of this account is {self.user.name}")
        print(f"gmail is {self.user.email}")
        print("..............................")
        for t in self.__transaction:
            print(t)
        print("...............................")

    def loan_from_bank(self,amount):
        if amount<0:
            print("Invalid amount....")
        elif self.loan_count>2 or self.flag_loan==False:
            print(f"the user of {self.account_number} has taken enough loan.pay the loan first...")
            self.flag_loan=False
        elif self.loan_count<=2 and self.flag_loan==True:
            self.__balance+=amount
            self.__transaction.append((datetime.now(),f"you got loan {amount}"))
            self.loan_count+=1
            self.loan+=amount
            print("you got loan from bank")

    def transfer_amount(self,amount,account_id):
        if amount<0:
            print("invalid amount")
        elif amount>self.__balance:
            print("Not enough balance in your account")
        elif account_id not in self.bank.account_count:
            print("Account does not exist”")
        else:
            self.bank.account_count[account_id].__balance+=amount
            self.__balance-=amount
            self.__transaction.append((datetime.now(),f"transfer {amount} BDT to {account_id}"))
            print("Transfer Success")

    def __repr__(self) -> str:
        print(f"The name of the account holder: {self.user.name}")
        print(f"email: {self.user.email}")
        print(f"address: {self.user.address}")
        print(f"account type: {self.user.account_type}")
        print(f"Balance: {self.__balance}")
        print(f"Taken loan from Bank: {self.loan_count}")
        return " "
        
            


    
    
        

        