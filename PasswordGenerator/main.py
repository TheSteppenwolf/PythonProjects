'''
Project done by: Sebastián Tamayo
Language: Python
Date: 03/04/2022
Description:
  A simple Password Generator with a lot of potential that can generate passwords with great length that can be personilized with the use lower-case letters as well as upper-case letters, numbers and especial symbols.
  The code was made as part of the course: 100 Days of Code: The Complete Python Pro Bootcamp for 2022
'''

import random
import password_module

print('''
---------------------------------------------------------
Welcome to PySewd Password Generator!

Here you can generate complicated passwords in order to give a more sophisticated sense of security to all your accounts!

---------------------------------------------------------
''')

length = int(input("Enter the length of the password: "))
upper_lower = input("Would you want the use the combination of lower and upper case? (Y/N): ").upper()
symbols = input("Would you want the use of special symbols? (Y/N): ").upper()
numbers = input("Would you like the use of numbers? (Y/N): ").upper()

# Variables
random_level = 0
random_char = 0
id_count = 0
password = ""

# Establishment of level of security
if upper_lower == "Y":
    id_count += 1
if numbers == "Y":
    id_count += 1
if symbols == "Y":
    id_count += 1
for letter in range(length): 
    # Takes random level of security
    random_level = random.randint(0,id_count)
    # Randomize the sequence inside the password
    random_char = random.randint(0, password_module.get_sizes(random_level)-1)
    password += (password_module.get_element(random_level,random_char))

# Prints out the password
print(f"You generated password is: {password}")
   
