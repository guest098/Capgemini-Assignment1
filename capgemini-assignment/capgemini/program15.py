def leap_year(n):
    if n%4==0 and (n%100!=0 or n%400==0):
        return True
    else:
        return False
def get_input():
    t=int(input('Enter the number of times to check given year:'))
    for i in range(t):
        n=int(input('Enter the year:'))
        if leap_year(n):
            print(n,'is a leap year')
        else:
            print(n,'is not a leap year')
def main():
    get_input()
main()