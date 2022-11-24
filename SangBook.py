import os
import pwinput
import random
import string


menu = ['Login', 'Logout', 'Exit']

logged_in = False



Account_crated = False

def menu_display(): # This is for displaying the menu
    for x in menu:
        print(x)
        

charactors = string.ascii_letters + string.digits + string.punctuation + " " # These are the characters for the password generator

global password



print('Welcome to SangBook')

def menus():
    
    menu_display()
    choose = input(f'Please choose one of the above options : ' ) .lower()
    


    if choose == 'login':
        
        # Checking if Account already exists
        
        if os.path.exists('Account_exists.txt'):
                global Account_crated
                Account_crated = True

        if os.path.exists('Account_password.txt'):
            with open('Account_password.txt', 'r') as password:
                password = str(password.read())                    
        if os.path.exists('Account_username.txt'):
            with open('Account_username.txt', 'r') as username:
                username = str(username.read())
        
        # When the account already exists

        while True:
            if Account_crated == True:
                input_username = input('Please enter your username : ')
                input_password = pwinput.pwinput('Please enter your password : ')
                
                
                
                if input_username == username and input_password == password:
                    print(f'Welcome {username.capitalize()}!')
                    break
                    
                else:
                    print('Please check your username and password again.')

             
        # If it dosent exists making a new one
                
            else:
                first_username = input('Please choose your username : ')
                with open('Account_username.txt', 'w') as username:
                    username.write(str(first_username))
                generate_password = input('Do you want to generate a reccomended password? (Yes/No) : ').lower()
                if generate_password == 'yes':
                      
                # Password generation
                
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
                                global saved_password
                                saved_password = password
                                with open('Account_password.txt', 'w') as password:
                                    password.write(str(saved_password))
                                with open('Account_exists.txt', 'w') as exists:
                                    exists.write(str('Account does exist'))
                                print('Ok! You have successfully created your account!')
                                menus()
                    generator()
                    
                # User input password
                
                
                else:
                    first_password = pwinput.pwinput('Please choose your password : ')
                    with open('Account_password.txt', 'w') as password: 
                        password.write(str(first_password))
                    with open('Account_exists.txt', 'w') as exists:
                        exists.write(str('Account does exist'))
                    
                    print('Ok! You have successfully created your account!')
                    menus()
    
    elif choose == 'logout':
        while True:
            if os.path.exists('Account_exists.txt'): # Checking if Account is already logged out
                with open('Account_password.txt', 'r') as verify_password:
                    verify_password = str(verify_password.read())
                verify = pwinput.pwinput('Please enter your account password : ')
                                         
                if verify == verify_password:
                    confirm = input('Are you sure you want to Logout? (Yes/No) : ').lower()  
                    
                    if confirm == 'yes':
                        while True:
                            
                            double_confirm = input('Please type "Confirm" to logout : ')
                            if double_confirm == 'Confirm':
                                
                                os.remove('Account_exists.txt')
                                os.remove('Account_password.txt')
                                os.remove('Account_username.txt')
                                print('You have successfully logged out!')
                                menus()
                                break
                    else:
                        print("Ok! You won't be logged off!")
                        menus()
                
                
                else:
                    print('Please check your password and try again')
            
            
            else:
                print('You have already logged out!')
                menus()
    
    else:
        print('Goodbye!')
        exit()
            
            
        
        
menus()