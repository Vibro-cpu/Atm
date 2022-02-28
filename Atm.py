Credentials_Screen = True
Allow_Access = False
Withdraw = False
Deposit = False
Exit = False

Card_Number = 7147546388701658
Pin_Number = 171975
Balance = 100

WithdrawText = "Withdraw"
DepositText = "Deposit"
ExitText = "Exit"

if (Credentials_Screen == True):
    Card_Input = input("Card Number : ")
    Pin_Input = input("Pin Number : ")

    if (Card_Input == 7147546388701658 and Pin_Input == 171975):
        Allow_Access = True
    else:
        Print = "Sorry, your Card or Pin number is incorrect, please try again.asd"

if (Allow_Access == True):
    print(Balance)
    Atm_Action_Input = input("Would you like to Withdraw or Deposit Cash? : ")

    if(Atm_Action_Input == WithdrawText):
        Withdraw = True
    else:
        Withdraw = False

    if(Atm_Action_Input == DepositText):
        Deposit = True
    else:
        Deposit = False

    if(Atm_Action_Input == ExitText):
        Exit = True
    else:
        Exit = False

if (Withdraw == True):
    WithdrawInput = input("How much would you like to withdraw? : ")
    Balance = WithdrawInput - Balance
    print(Balance)

if (Deposit == True):
    DepositInput = input("How much would you like to deposit? : ")
    Balance = DepositInput + Balance
    print(Balance)

if (Exit == True):
    ExitInput = input("Thanks for using this Atm!")