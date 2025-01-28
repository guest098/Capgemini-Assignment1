def display():
    print('1.Check the Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Exit')
def balance_checker(balance):
    print(f"Your current balance is: {balance}")
def deposit_money(amount,balance):
    balance+=amount
    print(f"You have deposited {amount}. Your new balance is {balance}")
    return balance
def withdraw_money(amount,balance):
    if amount > balance:
        print("Insufficient balance")
    elif amount <= 0:
        print("Invalid amount")
    else:
        balance-=amount
        print(f"You have withdrawn {amount}. Your new balance is {balance}")
def main():
    balance = 0
    while True:
        display()
        choice = int(input('Enter your choice: '))
        if choice==1:
            balance_checker(balance)
        elif choice==2:
            amount=float(input('Enter the amount to deposit: '))
            balance=deposit_money(amount,balance)
        elif choice==3:
            amount=float(input('Enter the amount to withdraw: '))
            balance=withdraw_money(amount,balance)
        elif choice==4:
            print(f'Exit the application')
            break
        else:
            print('Invalid choice')
main()

