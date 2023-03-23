# name = input("what is your name")
# age =input('what is your age')
# if age <="18" and age > "80" : 
#     print( "you are legal drive")
#     if age <=0 :
#         print( "you shouldnt drive")
# else :
#     print("you are grown masa go home")
 
bill = 0
print("welcome to lefam pizza")

size = input("which size do you want? L, M, S,: ")
add_pepperoni = input("do you want to add pepperoni? Y or N: ")
extra_cheese = input("do you want extra cheese? Y or N: ")

if size == "L":
    bill += 100
elif size == "M":
    bill += 85
else:
    bill += 50

if add_pepperoni == "Y":
    bill += 10

if extra_cheese == "Y":
    bill += 5  


print(f"the total bill is {bill}")    


