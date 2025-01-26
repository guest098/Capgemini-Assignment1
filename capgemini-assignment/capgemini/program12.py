def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
def get_input():
    n=int(input('Enter the n value to check for the pattern:'))
    return n
def main():
    n = get_input()
    pattern(n)
main()