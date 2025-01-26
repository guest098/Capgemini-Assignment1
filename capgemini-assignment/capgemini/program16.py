def even_or_odd(list):
    odd=[]
    even=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return f'Even list is :{even} and odd list is:{odd}'
def get_input():
    n=int(input("Enter the number of elements in the list:"))
    list=[]
    for i in range(n):
        x=int(input(f"Enter element {i+1}:"))
        list.append(x)
    return list
def main():
    list=get_input()
    print(even_or_odd(list))
main()