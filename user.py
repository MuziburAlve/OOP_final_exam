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