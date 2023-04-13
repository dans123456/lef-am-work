#grading system
"""
90 - 100 = A
80 - 89 = B
60 - 79 = C
40 - 59 = D
0 - 39 = F

"""
 

print("""
90 - 100 = A
80 - 89 = B
60 - 79 = C
40 - 59 = D
0 - 39 = F
    """)

userScore = int(input("enter your grade and dont be ashamed\n") )

if userScore <= 100 and userScore >95:
    print("A+")  
    elif userScore <= 95 :
        print("A")  
    elif userScore <= 89:
        print("B+")
    elif userScore <= 85:
        print("B-")
    elif userScore <= 79:
        print("C+")
    elif userScore <= 60 and userScore > 0:
        print("C")   
else:
    print("masa invalid")    