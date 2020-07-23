n = int(input("enter the number of rows "))
for i in range(1,n+1):
    print(" "*(n-i),end = '')
    for j in range(1,i+1):
        print(chr(65+n-j),end =' ')
    print()