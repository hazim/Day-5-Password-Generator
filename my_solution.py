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
  # this block could be further shortened by using the random.choice() option e.g.:
  # password += random.choice(letters) 
  letter_number = random.randint(1, len_letters)
  selected_letter = letters[letter_number]
  password += selected_letter

for symbol in range(1, nr_symbols + 1):
  symbol_number = random.randint(1, len_symbols)
  selected_symbol = symbols[symbol_number]
  password += selected_symbol

for number in range(1, nr_numbers + 1):
  number_number = random.randint(1, len_numbers)
  selected_number = numbers[number_number]
  password += selected_number

password
print("Generated logical password:", password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_length = len(password)
counter = 0
new_password_list = []
# seperating each digit in the string into a seperate list elements with will be inserted into the "new_password_list" empty list above 
for passlist in range(1, password_length + 1):
  new_password_list += password[counter]
  counter += 1

# shuffling the end new_password_list in order to randamize the digits in the password 
random.shuffle(new_password_list)
# combining all the list elements into a string without any spaces in between 
new_password = "".join(new_password_list)

print("Your new password is:", new_password)
