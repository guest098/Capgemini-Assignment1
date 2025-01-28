def second_largest_num(arr):
    if len(arr)<2:
        return None
    else:
        max_num=second_max=float('-inf')
        for num in arr:
            if num>max_num:
                second_max=max_num
                max_num=num
            elif num>second_max and num!=max_num:
                second_max=num
        return second_max if second_max!=float('-inf') else None
def get_input():
    n=int(input('Enter the size of an arr:'))
    arr=[]
    for i in range(n):
        num=int(input('Enter the number:'))
        arr.append(num)
    return arr
def main():
    arr=get_input()
    print(second_largest_num(arr))
main()