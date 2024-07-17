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
        
            
class User:
    def __init__(self,name,email,address,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        
    def create_account(self,Bank):
        Bank.creat_account(self.name,self.email,self.address,self.account_type)

    def deposit_money(self,account_id,bank,amount):
          bank.deposit_amount(account_id,amount)

    def withdraw(self,account_id,bank,amount):
        bank.withdraw_amount(account_id,amount)
        
    def check_available_balance(self,account_id,bank):
        bank.check_balance(account_id)

    def check_transaction_history(self,account_id,bank):
        bank.transaction_history(account_id)

    def loan_from_bank(self,bank,account_id,amount):
        bank.loan(account_id,amount)

    def transfer_amount(self,bank,amount,me_account_id,you_account_id):
        bank.transfer(amount,me_account_id,you_account_id)

class Admin:
    def __init__(self) -> None:
        self.name="ADMIN"
        self.password=1410777

    def check_pass_invalid_or_not(self,name,passw):
        if name!=self.name and passw!=self.password:
            return False
        else:
            return True
    def create_account(self,user,bank):
        bank.creat_account(user.name,user.email,user.address,user.account_type)

    def delete_user_account(self,bank,account_id):
        bank.delete_account(account_id)

    def block_w_t_feature(self,bank,button):
        bank.Bankrupt_option(button)

    def off_on_loan(self,bank,button):
        bank.loan_features_off_or_on(button)
     
    def see_all_account(self,bank):
        bank.see_all_account()
    
    def see_total_balance_of_bank(self,bank):
        print(f"total balance of bank is {bank.total_balance_of_bank()}")

    def see_total_loan(self,bank):
        print(f"Total loan of bank is {bank.total_loan()}")

class Bank:
    
    def __init__(self,name) -> None:
        self.name=name
        self.account_count={}
        self.__bankrupt=False
        self.__is_loan=True
        self.account_count_start=1410777247
        self.user=None
    
    @property
    def loann(self):
        return self.__is_loan
    
    @loann.setter
    def loann(self,value):
        self.__is_loan=value
    
    @property
    def bankrupt(self):
        return self.__bankrupt
    
    @bankrupt.setter
    def bankrupt(self,value):
        self.__bankrupt=value
    

    def creat_account(self,name,email,address,account_type):
        k=User(name,email,address,account_type)
        user = Account(k,self)
        l=self.account_count_start+1
        user.account_number=l
        self.account_count_start=l
        self.account_count[user.account_number]=user
        print("Account Created Successfully")
        print(f"your account ID is {user.account_number}")
    
    def deposit_amount(self,account_id,amount):
        if account_id in self.account_count:
            self.account_count[account_id].deposit(amount)
            
        else:
            print("this account id invalid or it dosen't even exits\n")
    
    def withdraw_amount(self,account_id,amount):
        if self.__bankrupt == False:
            if account_id in self.account_count:
               self.account_count[account_id].withdraw(amount)
        else:
            print("the bank is bankrupt\n")

    def check_balance(self,account_id):
         if account_id in self.account_count:
            self.account_count[account_id].available_balance()
            
         else:
            print("this account id invalid or it dosen't even exits")
        
        

    def transaction_history(self,account_id):
        if account_id in self.account_count:
           self.account_count[account_id].transaction_history()
            
        else:
            print("this account id invalid or it dosen't even exits")
        
        
    
    def loan(self,account_id,amount):
        if account_id in self.account_count:
           if self.__is_loan==True:
             self.account_count[account_id].loan_from_bank(amount)
           else:
               print(f"the user of this {account_id} can not take loan")         
        else:
            print("this account id invalid or it dosen't even exits")
        
    

    def transfer(self,money,your_account_id,other_account_id):
        if self.__bankrupt == False:
            if your_account_id in self.account_count:
               self.account_count[your_account_id].transfer_amount(money,other_account_id)
        else:
            print("the bank is bankrupt")



    
    def delete_account(self,account_number):
        if account_number in self.account_count:
            del self.account_count[account_number]
            print("Account deleted successfully")
        else:
            print("Account does not exist")

    def total_balance_of_bank(self):
        return sum(value.available_balance() for value in self.account_count.values())
    
    def total_loan(self):
        return sum(value.loan for value in self.account_count.values())
    

    def see(self):
        for key,value in self.account_count.items():
            print(self.account_count[key])
            
    def see_all_account(self):
        print("here is the account of all user:")
        for key,Value in self.account_count.items():
            print("................................................")
            print(f"account number {key}------->name: {Value.user.name}")
            print(Value.available_balance())

    def Bankrupt_option(self,f):
        self.bankrupt=f
    def loan_features_off_or_on(self,f):
        self.loann=f

Sonali_bank=Bank("Sonali Bank LTD")

#for Admin 
#user name-> ADMIN
#password--> 1410777
#otherwise you will get invalid
def Admin_____menu():
     User_name=input("Enter User name: ")
     password=int(input("Enter Password: "))
     Ad=Admin()
     check=Ad.check_pass_invalid_or_not(User_name,password)
     if check == True:
        while True:
            print("!!Welcome Admin!!")
            print("1.Create Account")
            print("2.Delete Account of a User")
            print("3.See all account list")
            print("4.Check Total Balance of Bank")
            print("5.Check total loan of Bank")
            print("6.block withdraw and transfer of all user")
            print("7.on or off loan feature of bank")
            print("8.Exit")

            op=int(input("Enter option:" ))

            if op==1:
                name=input("Enter name: ")
                email=input("Enter email: ")
                address=input("Enter address: ")
                print("what kind of account would you like to build!")
                print("1.Savings")
                print("2.Cuurent")

                op1=int(input("Enter account type: "))
                if op1==1:
                    human=User(name,email,address,"Savings")
                    Ad.create_account(human,Sonali_bank)
                    

                elif op1==2:

                    human=User(name,email,address,"Cuurent")
                    Ad.create_account(human,Sonali_bank)

                else:
                    print("invalid Option")

            elif op==2:

                op1=int(input("Enter account id for delete: "))
                Ad.delete_user_account(Sonali_bank,op1)

            elif op==3:

                Ad.see_all_account(Sonali_bank)

            elif op==4:

                Ad.see_total_balance_of_bank(Sonali_bank)

            elif op == 5:

                Ad.see_total_loan(Sonali_bank)

            elif op==6:

                print("If you want to off Enter 1")
                print("If you want to on Enter 2")
                op1=int(input("Enter option: "))
                if op1==1:
                       Ad.block_w_t_feature(Sonali_bank,True)
                       print("Withdraw and transfer blocked successfully")
                elif op1==2:
                    Ad.block_w_t_feature(Sonali_bank,False)
                    print("Withdraw and transfer unblocked successfully")
                else:
                    print("Invalid option")
            elif op==7:
                print("If you want to off loan features Enter 1:")
                print("If you want to on loan features Enter 2:")
                opp=int(input("Enter option: "))
                if opp==1:
                    Ad.off_on_loan(Sonali_bank,False)
                    print("Loan Blocked successfully")
                elif opp==2:
                    Ad.off_on_loan(Sonali_bank,True)
                    print("Loan UnBlocked successfully")
                else:
                    print("***Invalid Option***")
            elif op == 8:
                break
            else:
                print("Invalid Option")

     elif check ==False:
            print("****Invalid****")


def user_menu():
        name=input("Enter name: ")
        email=input("Enter email: ")
        address=input("Enter address: ")
        
        print("what kind of account would you like to build!")
        print("1.Savings")
        print("2.Cuurent")
        op=int(input("Enter option: "))
        if op==1:
            human=User(name,email,address,"Savings")
            human.create_account(Sonali_bank)
            
        elif op==2:
            human=User(name,email,address,"Cuurent")
            human.create_account(Sonali_bank)
        else:
            print("***Invalid***")
    
        while True:
            print(f"Welcome {name}")
            print("1.Deposit Money")
            print("2.Withdraw Amount")
            print("3. Check Available Balance")
            print("4.Check Transaction History")
            print("5.Take Loan From Bank")
            print("6.Transfer Money")
            print("7.Exit")
            op=int(input("Enter Option: "))
            if op==1:
                money=int(input("Enter the amount of money: "))
                op1=int(input("Enter account id: "))
                human.deposit_money(op1,Sonali_bank,money)
            elif op==2:
                money=int(input("Enter the amount of money: "))
                op1=int(input("Enter account id: "))
                human.withdraw(op1,Sonali_bank,money)
            elif op==3:
                op1=int(input("Enter account id: "))
                human.check_available_balance(op1,Sonali_bank)
            elif op==4:
                op1=int(input("Enter account id: "))
                human.check_transaction_history(op1,Sonali_bank)
            elif op==5:
                money=int(input("Enter the amount of money: "))
                op1=int(input("Enter account id: "))
                human.loan_from_bank(Sonali_bank,op1,money)
            elif op==6:
                money=int(input("Enter the amount of money: "))
                me_acc_id=int(input("Enter your Account number: "))
                he_acc_id=int(input("Enter your reciver Account number: "))
                human.transfer_amount(Sonali_bank,money,me_acc_id,he_acc_id)
            elif op==7:
                break
            else:
                print("***invalid***")



            

while True:
    print(f"Welcome to {Sonali_bank.name}")
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    option=int(input("Enter option: "))
    if option == 1:
        Admin_____menu()
    elif option == 2:
        user_menu()
    elif option == 3:
        break
    else:
        print("**Invalid**")

        

    
    
        

        