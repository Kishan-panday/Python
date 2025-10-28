# num1=int(input("Enter the first number: "));
# num2=int(input("Enter the second number: "));
# sum= num1+num2;
# print("sum of the number is",sum);

# x=float(input("Enter the number:"));
# print("Area:", x*x);

# x=int(input("Enter the number:"));
# y=int(input("Enter the number:"));
# if(x>=y):
#     print("True");

# else:
#     print("false");

# x=int(input("Enter the number:"));
# if(x%2==0):
#     print("even no.");
# else:
#     print("Odd no.");


def cal_fact(n):
    fact=1
    for i in range(1, n+1):
     fact *=i
    print(fact)


cal_fact(4)
    
