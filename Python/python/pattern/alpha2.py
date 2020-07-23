n = int(input("enter number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-i),end = ' ')
    print()