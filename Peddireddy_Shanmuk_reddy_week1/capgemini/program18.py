def calculate_bmi_eitherUnderweight_Normal_Overweight(weight,height):
    bmi=weight/(height**2)
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi<25:
        return "Normal"
    elif 25<=bmi<30:
        return "Overweight"
    else:
        return "Obese"
def get_input():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    return weight, height
def main():
    weight, height = get_input()
    print(calculate_bmi_eitherUnderweight_Normal_Overweight(weight, height))
main()

