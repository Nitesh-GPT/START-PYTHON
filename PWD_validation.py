import re

PWD = input("Enter the password: ")
PWD_len = len(PWD)
is_valid = False

while True:
    if PWD_len < 7 or PWD_len > 20: break
    elif not re.search ('[A-Z]', PWD): break
    elif not re.search ('[a-z]', PWD): break
    elif not re.search ('[0-9]', PWD): break
    elif not re.search('[@$#!]', PWD): break
    elif re.search('/s', PWD): break
    else:
        is_valid = True 
        break
if is_valid: 
    print("Password is valid")
else:
    print("No wrong password")



