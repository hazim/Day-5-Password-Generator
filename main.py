#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_string = ""
symbols_string = ""
numbers_string = ""

letters_length = len(letters)
# print(letters_length)

for l_string in range(1, nr_letters + 1):
  numb = random.randint(0, letters_length)
  choice = letters[numb]
  letter_select = choice
  letters_string += letter_select
  print(letters_string)

symbols_length = len(symbols)
print(symbols_length)

# for s_string in range(1, nr_symbols + 1):
#   numb1 = random.randint(0, symbols_length)
#   symbol_select = symbols[numb1]
#   symbols_string += symbol_select
  # print(symbols_string)



# for n_string in range(0, nr_numbers):
#   numb2 = random.randint(1, len(numbers))
#   number_select = numbers[numb2]
#   numbers_string += number_select
  # print(numbers_string) 

# password = str(f"{letters_string}{symbols_string}{numbers_string}")

# length = len(password)

# print(password, length)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_list = []
# counter = 0

# for each in password:
#   password_list.append(password[counter])
#   counter += 1

# print(password_list)

# shuffle_list = random.shuffle(password_list)

# new_password = ", ".join(shuffle_list)

# print(new_password)