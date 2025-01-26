def factorial(n):
    if n<0:
        return "Factorial does not exist for negative numbers"
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def factorial_using_loop(n):
    if n<0:
        return "Factorial does not exist for negative numbers"
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
def get_input():
    n=int(input('Enter the number to check for factorial:'))
    return n
def main():
    n=get_input()
    print("Factorial of",n,"is",factorial(n))
    print("Factorial of",n,"is",factorial_using_loop(n))
main()