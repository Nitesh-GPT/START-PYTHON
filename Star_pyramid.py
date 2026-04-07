'''pyramid printing using for loop

rows = int(input("Enter the number: "))
for i in range(1, rows+1):
    for j in range(1, rows-i + 1):
        print(end=' ')
    for star in range(1, i+1):
        print("*", end=' ')
    print('')'''
