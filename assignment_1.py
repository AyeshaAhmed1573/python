# Write a Python program to print the following string in a specific format (see the output).
print('''twinkle twinkle little star
     how i wonder what you are!
        Up above the world so high
        Like a diamond in the sky
twinkle twinkle little star
     how i wonder what you are!''')

# Write a Python program to get the Python version you are using

import sys
print(sys.version)

# Write a Python program to display the current date and time

from datetime import datetime
print(datetime.now())

# Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
radius= int(input("enter the radius of circle:"))
area=math.pi*radius**2
print(area)

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
firstname=input("enter your first name:")
lastname=input("enter your last name:")
print(lastname+" "+firstname)

# Write a Python program which takes two inputs from user and print their addition.
digit1=int(input("enter first number"))
digit2=int(input("enter second number"))
sum=digit1+digit2
print(sum)

# Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades.
total=500
maths=int(input("enter your maths marks:"))
english=int(input("enter your english marks:"))
science=int(input("enter your science marks:"))
urdu=int(input("enter your urdu marks:"))
computer=int(input("enter your computer marks:"))
if(maths>100 or science>100 or english>100 or urdu>100 or computer>100 or maths<0 or science<0 or urdu<0 or computer<0):
    print('invalid value')
else:
    sum = maths + english + science + urdu + computer
    percentage = (sum / total) * 100
    print("percentage: ", percentage)
    if percentage > 80 and percentage < 100:
        print("A+")
    elif percentage > 100:
        print("incorrect input")
    elif percentage < 80 and percentage > 70:
        print("A")
    elif percentage < 70 and percentage > 60:
        print("B+")
    elif percentage < 60 and percentage > 50:
        print("B")
    elif percentage < 50 and percentage >= 40:
        print("C")
    else:
        print("fail")
        
# Write a program which takes input from user and identify that the given number is even or odd.

value=int(input("enter your value:"))
if value%2==0:
    print("the number is even")
else:
    print("the number is odd")
