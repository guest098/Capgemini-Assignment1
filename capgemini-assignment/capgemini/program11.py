def password_checker_for_eightcharectors_include_upper_lower_digits_special(n):
    if len(n)>=8:
        if(any(c.islower() for c in n) and any(c.isupper() for c in n) and any(c.isdigit() for c in n) and any(c in"!@#$%^&*()_+-={}:<>?/" for c in n)):
            return True
        else:
            return False
def get_input():
    s=input('Enter the password:')
    return s
def main():
    s=get_input()
    if password_checker_for_eightcharectors_include_upper_lower_digits_special(s):
        print('Password is valid')
    else:
        print('Password is not valid')
main()