import string 
import random

# getting password length
len_pass = int(input('Enter password here: '))

print('''Create password from these set of characters:
      1. Digits
      2. Letters
      3. Special Characters
      4. Exit''')

char_list = ""

# Getting character set for Generated Password
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):

        # Addition for possible characters 
        char_list += string.ascii_letters
    elif(choice == 2):

        # Addition for possible digits in Passwords
        char_list += string.digits
    elif(choice == 3):

        # Addition for possible punctuations
        char_list += string.punctuation
    elif(choice == 4):
         break
    else:
        print("Select valid option :)")


password = []

for i in range(len_pass):

    # Selecting Random char. from our character list
    random_character = random.choice(char_list)

    # Append random characters to password
    password.append(random_character)

#password
print('Obtained Password is ' + ''.join(password))