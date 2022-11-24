# This is the password generator I used on the main programme.


import random
import string



charactors = string.ascii_letters + string.digits + string.punctuation + " "

global password



def generator():
    try:
        password_length = int(input('How many charactors would you like? : '))
        if password_length > len(charactors):
            new_charactors = password_length*charactors
            password = "".join(random.sample(new_charactors, password_length))
        else:
            password = "".join(random.sample(charactors, password_length))
    except ValueError:        
        print('Please enter only integer values please!')
        generator()
    except Exception as error:
        print('Something went wrong :(')
        print(error)
    else:
        print(f'Your generated password is {password}')
        differnt_password = input('Do you want to generate a different password? (Yes/No) : ').lower()
        if differnt_password == 'yes':
            generator()
        else:
            print(f'Ok, Your password is : {password}')
            saved_password = password

generator()


    
    
    








# password_length = int(input('How many charactors would you like? : '))
# password = "".join(random.sample(charactors, password_length))
# print(password)

