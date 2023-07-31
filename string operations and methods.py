my_name =()
first_name ="Datta"
last_name='sai'
profile=""" Sai is working in tundersoft. 
he completed his Btech in 2022. 
Recently he completed internship in c language . 
He is learnig Python as well."""
print("first name is {} ".format(first_name))
print("Last name is {} ".format(last_name))
print("Profile is {} ".format(profile))
a=10
b=20
c=a+b
print("sum of {} and {} is {}",c)
print("sum of {} and {} is {}".format(a,b,c))
print("sum of 10 and 20 is ",c)

full_name=first_name+last_name # string concatination
print("Full name is {}".format(full_name))

print(len(first_name))

spl_name='mani'
repeat_name=spl_name*80
print(repeat_name)
print("Profile is {} ".format(profile))
print(repeat_name)
print("Length of full name is {}".format(len(full_name))) # len function gives number of characters in the string

#Indexing and Slicing:
#'You can access individual characters in a string using indexing, where the first character has index 0. 
#Slicing allows you to extract a portion of a string.

str = "Hello"
print(str[0])        # Output: "H"
print(str[1:4])      # Output: "ell"
print(str[1:])       # Output: "ello"
print(str[:3])       # Output: "Hel"
print(str[-1])       # Output: "o" (last character)

#[start:end:step]
#[start:] 
#[:end]
str = "Hello"

print(str[0])        # Output: "H"
print(str[0:6:2])    # Output: "Hlo"
print(str[1:])       # Output: "ello"
print(str[:3])       # Output: "Hel"
print(str[-1])       # Output: "o" (last character)

#string split

Str="welcome to Python World"
l=Str.split()
print(l)


l=['welcome', 'to', 'Python', 'World']
str2=",".join(l)
print(str2)

#string methods

str = " Hello, World! "
print(str.lower())
print(str.upper())
print(str.lstrip())
print(str.strip())
print(str.rstrip())
print(str.replace("hello","hi"))
print(str.split(","))

#The join() method in Python is used to concatenate a sequence of strings with a specified separator.
names = ["Alice", "Bob", "Charlie"]
joined_names = ", ".join(names)
print(joined_names)  # Output: "Alice, Bob, Charlie"

#find() function is used to search for a substring within a string and returns the lowest

str = "Hello, World!"
index = str.find("World")
print(index)  # Output: 7

str = "Hello, World!"
index = str.find("Universe")
print(index)  # Output: -1

str = "Hello, World!"
index = str.index("World")
print(index)  # Output: -1

str = "Hello, World!"
index = str.index("Universe")
print(index)  # Output: -1





























 
