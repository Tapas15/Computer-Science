n = int(input("Enter number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j,end = ' ') # i is column , j is row
    print()