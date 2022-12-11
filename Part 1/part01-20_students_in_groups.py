# Write your solution here
number_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
number_groups1 = number_students / group_size
number_groups2 = number_students // group_size
if number_groups1 == number_groups2:
    print("Number of groups formed: ", number_groups2)
else:
    print("Number of groups formed: ", number_groups2 + 1)