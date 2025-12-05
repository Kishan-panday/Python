a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if (a>b) and (a>c):
    print(f"{a} is max")
elif (b>c) and (b>a):
    print(f"{b} is max")
else:
    print(f"{c} is max")

