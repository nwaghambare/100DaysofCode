import random

print("Welcome to the PyPassword Generator")
num_let = int(input("How many letters would you like in your password?\n"))
num_sym = int(input("How many symbols would you like?\n"))
num_num = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

passlist = []
for char in range(num_let):
    passlist.append(random.choice(letters))

for char in range(num_sym):
    passlist.append(random.choice(symbols))

for char in range(num_num):
    passlist.append(random.choice(numbers))

random.shuffle(passlist)
password = ''.join(passlist)
print(f'Your password is\n{password}')