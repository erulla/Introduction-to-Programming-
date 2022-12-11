# Write your solution here
frequency= int(input("How many times a week do you eat at the student cafeteria? "))
price= float(input("The price of a typical student lunch? "))
money= float(input("How much money do you spend on groceries in a week? "))
total= frequency*price + money
daily= total/7
print("Average food expenditure: ")
print("Daily: " +str(daily) + " euros")
print("Weekly: " + str(total)+ " euros")