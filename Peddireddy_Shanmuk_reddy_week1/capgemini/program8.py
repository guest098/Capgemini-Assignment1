def multiplication_of_number(n):
    if(n==0):
        print("Enter the valid")
    for i in range(1,11):
        print(n,"*",i,"=",i*n)
def get_input():
    n=int(input('Enter the number to print table:'))
    return n
def main():
    n=get_input()
    multiplication_of_number(n)
main()