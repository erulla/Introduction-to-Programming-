# Write your solution here
limit = int(input("Upper limit: "))
base = int(input("Base: "))
exponent = 0
while (base**exponent) <= limit:
    print(base**exponent)
    exponent+=1