# Python Temperature Unit Converter (Celsius / Fahrenheit / Kelvin)

temp = float(input("Enter temperature: "))

Unit1 = input("This temperature is in the form of C / F / K: ")
Unit2 = input("You want to convert it into (C / F / K): ")

if Unit1 == "C" and Unit2 == "F":
    result = temp * 1.8 + 32
    print(f"The temperature is {round(result, 2)} F")

elif Unit1 == "F" and Unit2 == "C":
    result = (temp - 32) / 1.8
    print(f"The temperature is {round(result, 2)} C")

elif Unit1 == "K" and Unit2 == "C":
    result = temp - 273.15
    print(f"The temperature is {round(result, 2)} C")

elif Unit1 == "K" and Unit2 == "F":
    result = (temp - 273.15) * 1.8 + 32
    print(f"The temperature is {round(result, 2)} F")

elif Unit1 == "C" and Unit2 == "K":
    result = temp + 273.15
    print(f"The temperature is {round(result, 2)} K")

elif Unit1 == "F" and Unit2 == "K":
    result = (temp - 32) * (5 / 9) + 273.15
    print(f"The temperature is {round(result, 2)} K")

else:
    print("Invalid units entered. Please try again.")
