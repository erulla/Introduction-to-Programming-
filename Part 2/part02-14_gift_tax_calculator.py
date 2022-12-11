# Write your solution here
value=float(input("Value of gift: "))
tax=float(1)
rate=float(0.01)
if value>= 1000000:
    print(f"Amount of tax: {142100*tax + (17*rate)*(value-1000000)} euros")
elif value>=200000:
    print(f"Amount of tax: {22100*tax + (15*rate)*(value-200000)} euros")
elif value>=55000:
    print(f"Amount of tax: {4700*tax + (12*rate)*(value-55000)} euros")
elif value>=25000:
    print(f"Amount of tax: {1700*tax + (10*rate)*(value-25000)} euros")
elif value>=5000:
    print(f"Amount of tax: {100*tax + (8*rate)*(value-5000)} euros")
else:
    print("No tax!")
#model solution, shorter
#value = int(input("Value of gift: "))
 
#if value < 5000:
#    tax = 0
#elif value <= 25000:
#    tax = 100 + (value - 5000) * 0.08
#elif value <= 55000:
#    tax = 1700 + (value - 25000) * 0.10
#elif value <= 200000:
#    tax = 4700 + (value - 55000) * 0.12
#elif value <= 1000000:
#    tax = 22100 + (value - 200000) * 0.15
#else:
#    tax = 142100 + (value - 1000000) * 0.17
 
#if tax == 0:
#    print("No tax!")
#else:
#    print(f"Amount of tax: {tax} euros")
