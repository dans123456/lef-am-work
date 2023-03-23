"""
Write a python script that takes input from a user ansd displays it to the user ina well foramtted output
(use the concept of lists)
"""
userDetails = []
userinput = input('enter a name: ')
userDetails.append(userinput)
userinput = input('enter age: ')
userDetails.append(userinput)
userinput = input('enter class: ')
userDetails.append(userinput)
userinput = input('user gender: ')
userDetails.append(userinput)
userinput = input('enter telephone number: ')
userDetails.append(userinput)

print(f'your name is {userDetails[0]}. your name is {userDetails[1]}  ')
#adding a  dictionary will be  dic{}
#dic["name"]= name 