def grading(name,marks):
    mark=sum(marks)
    percentage=(mark*100)//500
    for i in marks:
        if percentage>=80:
            return f"{name} scored {percentage}% and is in A grade and got {mark} marks"
        elif percentage>=60:
            return f"{name} scored {percentage}% and is in B grade and got {mark} marks"
        elif percentage>=40:
            return f"{name} scored {percentage}% and is in C grade and got {mark} marks"
        else:
            return f"{name} scored {percentage}% and is in D grade and got {mark} marks"
def get_input():
    name=input("Enter your name:")
    marks=int(input('Enter the number of subjects marks'))
    arr=[]
    for i in range(marks):
        mark=int(input())
        arr.append(mark)
    return name,arr
def main():
    name,arr=get_input()
    print(grading(name,arr))
main()
