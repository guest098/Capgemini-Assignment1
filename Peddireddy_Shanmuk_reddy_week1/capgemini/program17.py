def count_each_occurences_of_word(s):
    words=s.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
def get_input():
    s=input('Enter the String:')
    return s
def main():
    s=get_input()
    print(count_each_occurences_of_word(s))
main()