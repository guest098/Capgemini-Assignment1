def program_to_print_from_1_to_100():
    for i in range(1,101):
        print(i)
    return
def program_to_print_buzz_fizz_bizzfizz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(f"{i} is BizzFizz")
        elif (i%3==0):
            print(f"{i} is Bizz")
        else:
            print(f"{i} is Fizz")
def main():
    program_to_print_from_1_to_100()
    program_to_print_buzz_fizz_bizzfizz()
main()