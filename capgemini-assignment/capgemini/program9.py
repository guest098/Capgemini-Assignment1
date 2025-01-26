def counting_vowels_consonants_digits_special_charcters(n):
    s=n.lower()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    digits = '0123456789'
    special_chars = '!"#$%&\'()*+,-./:;<=>?@[\\'
    count_vowels=0
    count_consonants=0
    count_digits=0
    count_special_charcters=0
    for i in s:
        if i in vowels:
            count_vowels+=1
        if i in consonants:
            count_consonants+=1
        if i in digits:
            count_digits+=1
        if i in special_chars:
            count_special_charcters+=1
    return count_vowels,count_consonants,count_special_charcters,count_digits
def get_input():
    n = input("Enter a string: ")
    return n
def string_reverse(s):
    return s[::-1]
def main():
    n = get_input()
    print(counting_vowels_consonants_digits_special_charcters(n))
    print(string_reverse(n))
main()