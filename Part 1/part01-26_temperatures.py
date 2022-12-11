# Write your solution here
temperature = int(input("Please type in a temperature (F): "))
convert = (temperature-32)*5/9
condition = convert < 0
print(f"{temperature} degrees Fahrenheit equals {convert} degrees Celsius")
if condition:
    print("Brr! It's cold in here!")