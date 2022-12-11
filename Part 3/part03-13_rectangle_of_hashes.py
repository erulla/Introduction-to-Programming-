# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))
symbol = "#"
 
while height > 0:
    print(width*symbol)
    height -= 1