'''here we will learn about the regular expressin which helps us
 to validate password, specified string forthe search pattern 
 (^) carrot symbol= (start with)used to check fromthe starting  
 [a, z] squire barcket= used to check that atleast one character is present in the given 
 string or password from a to z.    
 $ doller= (end with) doller symbol helps us to check the end string, matches or not.

import re
PWD = input("Enater the password to check:")

if re.search('^hello', PWD):
if re.search('gupta$', PWD):    
    print("the given string start with gupta")
else:
    print("no match SORRY!")



this \s helps us to know about the space in the provided text exist or not 
it return the first space in the string 

import re
txt= 'hey guys how is you doing today'
print(re.search('\s', txt).span())