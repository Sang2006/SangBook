# This is just a space where I test stuff before I add it to the main project

import string


password = input('Please enter your password : ')

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])


charactors = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()
    
if password in common_passwords:
    print("Password was found in a common password list. Score 0 / 10")
    exit()


if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1
    
print(f"Password length is {str(length)}, adding {str(score)} points!")


if sum(charactors) > 1:
    score += 1
if sum(charactors) > 2:
    score += 1
if sum(charactors) > 3:
    score += 1
print(f"Password has {str(sum(charactors))} different charactor types, adding {str(sum(charactors) -1)} points!")

if score < 4:
    print(f"Your passwors is weak! Score : {str(score)} / 7")
elif score == 4:
    print(f"Your passwors is ok! Score : {str(score)} / 7")
elif score > 4 and score < 6:
    print(f"Your passwors is good! Score : {str(score)} / 7")
elif score > 6 :
    print(f"Your passwors is srong! Score : {str(score)} / 7")
    