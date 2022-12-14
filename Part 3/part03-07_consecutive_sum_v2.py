# Write your solution here
limit = int(input("Limit:"))
number = 1
value = 1
statement = "1"
while value < limit:
    number += 1
    value += number
    statement += f" + {number}"
print(f"The consecutive sum: {statement} = {value}")