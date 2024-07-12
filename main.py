from bank import Bank
from account import Account
from user import User,Admin

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
            print("6.on or off loan feature of bank")
            print("7.Exit")

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

                print("If you want to off loan feature Enter 1")
                print("If you want to on loan feature Enter 2")
                op1=int(input("Enter option: "))
                if op1==1:
                       Ad.loan_feature(Sonali_bank,"off")
                elif op1==2:
                    Ad.loan_feature(Sonali_bank,"on")
                else:
                    print("Invalid option")

            elif op == 7:
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

        
