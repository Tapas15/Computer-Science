n = int(input("enter number "))
for i in range(1,1+n):
    print(" "*(i-1), end ="")
    for j in range(1,2+n-i):
        print(j,end =" ")
    print()