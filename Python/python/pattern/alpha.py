n = int(input("enter number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end = ' ') # character 64 ascii character after that character will print
    print()