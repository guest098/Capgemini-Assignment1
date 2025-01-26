def prime_or_not(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def prime_with_in_range(start,end):
    primes = []
    if start >=end:
        return "Enter the valid range"
    for i in range(start,end+1):
        if prime_or_not(i):
            primes.append(i)
    return primes
def get_input():
    start=int(input('Enter the start of the range:'))
    end=int(input('Enter the end of the range:'))
    return start,end
def main():
    start,end = get_input()
    print(prime_with_in_range(start,end))
main()