def palindrome_check_for_string_or_number(s):
    if s==s[::-1]:
        return True
    else:
        return False
def get_input():
    t=int(input('Enter the number of test cases:'))
    for i in range(t):
        s = input('Enter a string or number: ')
        if palindrome_check_for_string_or_number(s):
            print("The string or number is a palindrome")
        else:
            print("The string or number is not a palindrome")
def main():
    get_input()
main()