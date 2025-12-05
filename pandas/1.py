# import pandas as pd

# df = pd.read_csv("CollegePlacement.csv",encoding="latin1")
# print(df)
# print(df.info())
# print("First five")
# print(df.head())


# print("Last five")
# print(df.tail())
# print("describe")
# print(df.describe)
# print("select single column")
# print(df["CGPA"])
# print("more CGPA")
# print(df[df["CGPA"]>9])



# print("Enter new column:")
# df["SGPA"]= df["CGPA"]-3
# print(df)








# a= float(input("Enter the number:"))

# if a==0:
#  print("Number is zero")
# elif a>0:
#  print("+ve number")
# else:
#  print("-ve number")







# n1= float(input("Enter the first number:"))
# n2= float(input("Enter the Second number:"))
# n3= float(input("Enter the third number:"))

# if (n1>=n2) and (n1>=n3):
#     largest= n1
# elif (n2>=n1) and (n2>=n3):
#     largest= n2

# else:
#     largest=n3

# print(f"The largest number{largest}")    
    






def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
    
num = int(input("Enter the number"))
print(f"The factorial of a number: {num} is {factorial(num)} ")   

    


                    
                    