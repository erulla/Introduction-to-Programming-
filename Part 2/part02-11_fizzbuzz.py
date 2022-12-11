# Write your solution here
number=int(input("Number: "))
word1=str("Fizz")
word2=str("Buzz")
if number % 15 == 0:
    print(word1+word2)
elif number % 3 == 0:
    print(word1)
elif number % 5 == 0:
    print(word2)