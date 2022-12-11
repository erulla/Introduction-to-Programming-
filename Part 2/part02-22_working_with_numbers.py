# Write your solution here
attempts = 0
positive = 0
negative = 0
total = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number=int(input("Number: "))
    total+= number
    if number != 0:
        attempts +=1
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1 
    if number == 0:
        break
    
print(f"Numbers typed in {attempts}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total/attempts}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
