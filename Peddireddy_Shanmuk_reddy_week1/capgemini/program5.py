def display_menu():
    print('1.Adding the item to the menu')
    print('2.View the item to the menu')
    print('3.Calculate the total price')
    print('4.Exit')
def add_item(cart):
    name = input('Enter the name of the item: ')
    price = float(input('Enter the price of the item: '))
    cart.append({'name': name, 'price': price})
    print('Item added to the menu')
def view_item(cart):
    for i in range(len(cart)):
        print(f'{cart[i]["name"]}-${cart[i]["price"]:.2f}')
def calculate_total(cart):
    total = 0
    for item in cart:
        total+=item['price']
    print(f'The total price is {total}')
def main():
    cart=[]
    while True:
        display_menu()
        choice=int(input('Enter the option you want to proceed'))
        if choice==1:
            add_item(cart)
        elif choice==2:
            view_item(cart)
        elif choice==3:
            calculate_total(cart)
        elif choice==4:
            print(f'Exit the service')
        else:
            print('Invalid option')
main()
