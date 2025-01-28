def bank_loan_eligiblity(salary,age,creditscore):
    if salary>50000 and age>25 and creditscore>700:
        return "Loan is Approved because you are salary and age and creditscore was too good"
    else:
        return "Loan is not approved because you are salary or age or creditscore was too bad"
def get_input():
    salary = int(input("Enter your salary: "))
    age = int(input("Enter your age: "))
    creditscore = int(input("Enter your credit score: "))
    return salary,age,creditscore
def main():
    salary,age,creditscore = get_input()
    print(bank_loan_eligiblity(salary,age,creditscore))
main()
