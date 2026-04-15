''' RANGE(start, stop, step) 
FOR LOOP: used to print something certain number of time
for i in range(1, 5, 2):
    print(i)
print("we are done")

n = int(input("Enter the number:"))
sum = 0

for i in range(1, n+1):
    sum +=i

print( f"  the some of {n} number is {sum}")

#PRINT THE INPUT VALUE IN REVERSE ORDER 

n = int(input("Enter the numer for reverse:"))
for i in range(n, 0, -1):
    print(i)
print("Done!")    

@PRINT REVERSED NUMBER USING REVERSED() METHOD

n = int(input("enter the number:"))
for i in reversed(range(0, n, 1)):
  print(i)
@TO ACCESS THE ITEM OF AN VARIABLE USING FOR LOOP ?
name = "Niteshgupta"
for i in name:
    print(i, end=' ')

@access item in reverse order using for loop
name = "niteshgupta"
for i in name[:: -1]:
   print(i)


@temporary method to know the number of string in sentence
name = "hellohui"
count = 0
for i in name[0 :]:
 count +=1    
 print(count) 
 print(i)

#List comprehension for loop short syntax
cars = ['bmw', 'ferari', 'bugati']
[print(car) for car in cars]


#@Dictionary access by for loop method

Details = {'name':'nitesh', 'age': 20}
for detail, name in Details.items():
  print(detail, name)


@ for loop along with if conition to check specific item in the list
lists = ['python', 'java', 'c', 'js', 'react']
for list in lists:
    if 'java'== list:
        print("i like java")
        break
else: 
    print("i don't like java")  

n = 0
while n<=10:
    n +=1
    if n % 2 !=0:
        continue
    print(n, end=' ')       

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

for i in list1:
    for j in list2:
        print(i, j)
    print()


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

i = 0

while i < len(list1):
     j = 0
     while j < len(list2):
        print(list1[i], list2[j])
        j += 1

print()
i +=1       

WRITE PROGRAM TO SEPRATE EVEN AND ODD NUMBER IN A LIST USING FOR LOOP IN RANGE 25

li = list(range(1, 25))
even_number = []
odd_number = []
for item in li:
    if item % 2 == 0:
        even_number.append(item)
    else:
         odd_number.append(item)
print(even_number)
print(odd_number) '''



        
    



