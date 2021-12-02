# DEFINING ALL THE 'PROGRAM LOGIC' FUNCTIONS
# main menu function - displays the main menu
def main_menu():

    print('\n' * 100)
    print("        **Unit Converter**       \n")
    print("1. Degrees: Fahrenheit --> Celsius")
    print("2. Length: Inches --> Meters")
    print("3. Weight: Pounds --> Kilograms")
    print("4. Volume: Gallons --> Liters")
    print("5. Speed: MPH --> KPH\n")


# user input function
def user_input():
    option = None

    while option not in ['1', '2', '3', '4', '5']:
        option = input("Please enter a valid option: ")

    return option


# converting another? return True if yes and quit if False
def convert_another():

    opt = input("Convert another? Y/N ")

    if opt == 'Y' or opt == 'y':
        return True
    else:
        return False


# DEFINING ALL THE CALCULATIONS' FUNCTIONS
# degrees Fahrenheit to degrees Celsius
def deg_cel():

    x = int(input("Enter value in Fahrenheit: "))

    y = round((x - 32) * 5/9, 2)

    print(f'{x} degrees Fahrenheit is equal to {y} degrees Celsius'.format(x, y))


# inches to meter
def len_met():

    x = int(input("Enter value in inches: "))

    y = round((x / 39.37), 2)
    print(f'{x} inches is equal to {y} meters'.format(x, y))


# ounces to kilograms
def wei_kil():

    x = int(input("Enter value in pounds: "))

    y = round(x * 0.45359237, 2)
    print(f'{x} pounds is equal to {y} kilograms'.format(x, y))


# liters to gallons
def vol_lit():

    x = int(input("Enter value in gallons: "))

    y = round(x * 3.785, 2)
    print(f'{x} gallons is equal to {y} liters'.format(x, y))


# MPH to KPH
def mph_kph():

    x = int(input("Enter value in miles: "))

    y = round(x * 1.609, 2)
    print(f'{x} miles is equal to {y} kilometers'.format(x, y))
