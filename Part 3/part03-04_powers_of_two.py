# Write your solution here
limit = int(input("Upper limit: "))
number = 0
while (2**number) <= limit:
    print(2 ** number)
    number+=1