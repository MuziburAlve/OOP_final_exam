from account import Account
from user import User
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