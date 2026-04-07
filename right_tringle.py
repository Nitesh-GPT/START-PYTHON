'''to print the this tringle we need to understand outer and inner loop
which control the printing like i and j outer represent the rows and inner
represent the column.

rows = int(input("Enter the numer: "))
for i in range(1, rows+1):
  for j in range(1, i+1):
    print(i, end=' ')
  print(" ")

  print the tringle multiplication table 


rows = int(input("Enter the the bro.: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        multiply = i*j
        print(multiply, end=' ')
    print('') '''