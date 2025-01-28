def temperature_conversion_from_celsius_to_fearenheit(n):
    return (n*9/5)+32
def temperature_conversion_from_fahrenheit_to_celsius(n):
    return (n-32)*5/9
def temperature_conversion_from_celsius_to_kelvin(n):
    return n+273.15
def temperature_conversion_from_fahrenheit_to_kelvin(n):
    return (n-32)*5/9+273.15
def temperature_conversion_from_kelvin_to_celsius(n):
    return n-273.15
def temperature_conversion_from_kelvin_to_fahrenheit(n):
    return (n-273.15)*9/5+32
def main():
    print("Temperature Conversion Program")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = float(input("Enter temperature in Celsius: "))
        print(f"{n} degree Celsius is equal to {temperature_conversion_from_celsius_to_fearenheit(n)}")
    elif choice==2:
        n = float(input("Enter temperature in Fahrenheit: "))
        print(f"{n} degree Fahrenheit is equal to {temperature_conversion_from_fahrenheit_to_celsius(n)}")
    elif choice==3:
        n = float(input("Enter temperature in Celsius: "))
        print(f"{n} degree Celsius is equal to {temperature_conversion_from_celsius_to_kelvin(n)}")
    elif choice==4:
        n = float(input("Enter temperature in Fahrenheit: "))
        print(f"{n} degree Fahrenheit is equal to {temperature_conversion_from_fahrenheit_to_kelvin(n)}")
    elif choice==5:
        n = float(input("Enter temperature in Kelvin: "))
        print(f"{n} degree Kelvin is equal to {temperature_conversion_from_kelvin_to_celsius(n)}")
    elif choice==6:
        n = float(input("Enter temperature in Kelvin: "))
        print(f"{n} degree Kelvin is equal to {temperature_conversion_from_kelvin_to_fahrenheit(n)}")
main()