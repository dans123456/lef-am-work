"""
write a script for an average calculator
first u find the number of inputs  let say 4 using dis to store de loop then u store de number of inputs by adding it
u sum to the previous ones  den now u find the average of the inputs
"""
# SCRIPT FOR AN AVERAGE CALCULATOR 
values = []
total = 0
n= int(input("enter total number of values: "))
for numbers in range(n):
    num=int(input("ENTER A VALUE: "))
    values.append(num)
    total = total+ values[numbers]
print(total)    
average = total/n
print(average)


