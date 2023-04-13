# relational operators
# is not equal to we use the the exclamation and eqaul to !=
#logical operational 
#operands are what the signs are working on
# a = 12 
# b = 9
# print(a < b and a != b)
# #when using the and condition whatever u say should be true 
# level = int(input("enter your level: "))
# gpa = float(input("enter yah gpa: "))

# print(level >= 300 and gpa >= 2)
#when using the or it caters for  only one
#the modulo is %




# """
# basic if statements  with relational and logical operators
# """
# first_num = int(input("enter yah first number: "))
# second_num = int(input("enter yah second number: "))

# if(first_num > second_num):
#     print(f"{first_num} is greater than {second_num}")
# else :
#     print(f"{second_num} is greater than {first_num}")

"""
1. transfer money
2.MomoPay and Pay Bills
3. Airtime and Bundles

#transfer mooney 
1.Momo user
2.Non-momo user
3.send with care

"""

print("""
1. transfer money
2. MomoPay and Pay Bills
3. Airtime and Bundles

""")

userinput = int(input())
if userinput == 1:
    print("""
    1. transfer money
    2. MomoPay and Pay Bills
    3. Airtime and Bundles
    """)


    #nested if statement
    userinput = int(input())

    if userinput == 1:
        print("momo user.......")
    elif userinput == 2:
        print("Non-momo user.....")    
    else:
        print("bossu ebi invalid..........")    

elif userinput == 3:
        print("send with care.........")    
elif userinput == 2:
    print("#MomoPay...........")    
elif userinput == 3:
    print("#Airtime...........")
else:
    print("invalid input..... kwasia try again.....")















