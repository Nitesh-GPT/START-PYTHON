'''this program will prints the the sandglas pyramid  
shape.
rows = int(input("Enter the rows: "))
for i in range(rows, 0, -1):
    for space in range(1, rows-i +1):
       print(end=' ')
    for star in range(1, i + 1):
        print("*", end=' ')
    print("")
for j in range(1, rows+1):
    for jspace in range(1, rows-j +1):
        print(end=' ')
    for stars in range(1, j+1):
        print("*",end=' ')
    print('')
