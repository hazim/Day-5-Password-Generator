#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

len_letters = len(letters) - 1
len_symbols = len(symbols) - 1
len_numbers = len(numbers) - 1 

password = ""

for letter in range(1, nr_letters + 1):
  letter_number = random.randint(1, len_letters)
  selected_letter = letters[letter_number]
  password += selected_letter
  # print(password)

for symbol in range(1, nr_symbols + 1):
  symbol_number = random.randint(1, len_symbols)
  selected_symbol = symbols[symbol_number]
  password += selected_symbol
  # print(password)

for number in range(1, nr_numbers + 1):
  number_number = random.randint(1, len_numbers)
  selected_number = numbers[number_number]
  password += selected_number
  # print(password)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
