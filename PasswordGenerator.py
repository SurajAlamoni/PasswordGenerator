# PyPassword Generator
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['%','!','#','$','*']

value = int(input("how many alphabets do u want"))
numbs = int(input("how many numbers do u want"))
ch = int(input("how many symbols do u want"))

password = []
for n in range(1,value+1):
    password += random.choice(alphabets)

for n in range(1,numbs+1):
    password += random.choice(numbers)

for n in range(1,ch+1):
    password += random.choice(chars)

random.shuffle(password)
print(password)

final = ""
for c in password:
    final += c
    
print(final)
