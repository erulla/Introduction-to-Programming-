# Write your solution here
sentence =""
last=""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last:
        break
    sentence += word + " "
    last = word
print(sentence)