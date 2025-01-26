def bill_spliter_among_group_of_people(totalbillamount,numberofpeople,tippercentage):
    tip_amount=(totalbillamount*tippercentage)/100
    total_amount_to_be_paid=totalbillamount+tip_amount
    amount_each_person_has_to_pay=total_amount_to_be_paid/numberofpeople
    return amount_each_person_has_to_pay
def get_input():
    total_bill_amount=float(input("Enter the total bill amount: "))
    number_of_people=int(input("Enter the number of people: "))
    tip_percentage=int(input("Enter the tip percentage: "))
    return total_bill_amount, number_of_people, tip_percentage
def main():
    total_bill_amount, number_of_people, tip_percentage = get_input()
    amount_each_person_has_to_pay = bill_spliter_among_group_of_people(total_bill_amount,number_of_people,tip_percentage)
    print(f"Each person has to pay: {amount_each_person_has_to_pay}")
main()