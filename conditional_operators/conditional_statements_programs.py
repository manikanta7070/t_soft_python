'''# we have 3 flow flow control statements
#1. conditional statements 2.iterative statements 3.treansfer statements
print("______________________________________________________________")
#conditional statements

#1. simple if
a = 2
b = 5

if a<b:
    print('{} is less than {}'.format(a,b))
    print(a, 'is less than', b)
print("not satisfied the condition")

print("______________________________________________________________")
#If Statement where Boolean Expression is False
a = 13
b = 5
if a<b:
    print('{} is less than {}'.format(a,b))
print("not satisfied the condition")

print("______________________________________________________________")

#If statement with compound condition
a = 2
b = 5
c = 4
if a<b and a<c:
   print(a, 'is less than', b, 'and', c)
   
name_1= "mani"
name_2= "karthik"
name_3= "govindh"
if len(name_1)<len(name_2)and len(name_1)<len(name_3):
    print('{} is shorter than {}and {}'.format(name_1,name_2,name_3))

#If statement with condition evaluating to a number

a = 2

if a:
    print(a, 'is not zero')

#If statement with multiple statements in if-block
a = 10

if a > 2 :
    print(a, 'is not zero')
    print('{} is a even number'.format(a))
    print('{} is a greater than 2'.format(a))
print("------------------------------------------")

#if else:
#even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Program to check if a number is positive or negative
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")
    
#another model
    
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Positive and Even")
else:
    print("Not Positive and Even")'''


#Program to check if a year is a leap year:
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")

#Program to check if a character is a vowel or consonant:

ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("It's a vowel.")
else:
    print("It's a consonant.")
    
#Program to check if a number is a multiple of 3 or 5:

num = int(input("Enter a number: "))
if num % 3 == 0 or num % 5 == 0:
    print("Multiple of 3 or 5.")
else:
    print("Not a multiple of 3 or 5.")

#Program to check if a string is empty or not:

text = input("Enter a string: ")
if not text:
    print("The string is empty.")
else:
    print("The string is not empty.")

#Program to check if a student passed or failed based on marks

marks = eval(input("Enter student's marks: "))
if marks >= 50:
    print("Congratulations! You passed.")
else:
    print("Sorry, you failed.")

#True or false

i=100
if i==100:
 print("true")
else:
 print("false")

# program to check the given number is in between 1 and 100

n=int(input("Enter number:"))
if n>=1 and n<=100:
 print("The number",n,"is in between 1 to 100")
else:
 print("The number", n, "is not in between 1 to 100")


#nested if

#Program to check if a number is positive, negative, or zero using nested if:

num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

#leap year

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Program to check if a number is within a range using nested if
    
num = int(input("Enter a number: "))
if num >= 0:
    if num <= 100:
        print("Number is within the range.")
    else:
        print("Number is greater than 100.")
else:
    print("Number is less than 0.")


#Program to find the largest of three numbers using nested if
    
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a >= b:
    if a >= c:
        print(f"{a} is the largest.")
    else:
        print(f"{c} is the largest.")
else:
    if b >= c:
        print(f"{b} is the largest.")
    else:
        print(f"{c} is the largest.")

#elif

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter.")
elif ch.islower():
    print("Lowercase letter.")
elif ch.isdigit():
    print("Digit.")
else:
    print("Not an uppercase letter, lowercase letter, or digit.")


#Program to determine the category of a student's grade using nested if:
    
marks = float(input("Enter student's marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")    

#Program to check if a number is positive, negative, or zero using nested if-elif:

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


#Program to calculate the tax based on income using nested if

    income = float(input("Enter your income: "))

if income <= 500000:
    tax = 0
elif income <= 1000000:
    tax = (income - 500000) * 0.1
else:
    tax = 500000 * 0.1 + (income - 1000000) * 0.2

print(f"Tax: {tax}")
















    




















    
       






















    

















