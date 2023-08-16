#Type of Arguements
#=================
#1. positional arguments
#2. keyword arguments
#3. default arguments
#4. Variable length arguments

#1. positional arguments

def sub(a,b):
 print("sub is:",a-b)
sub(20,10)
sub(10,20)
sub(10,20,30) #TypeError: sub() takes 2
#positional arguments but 3 were given

#2. keyword arguments
#Ex:
def f1(name,msg):
 print("Hello:",name,msg)
#keyword arguments
f1(name="mohan",msg="Good morning")
f1(msg="Good morning",name="mohan")
#positional arguments
f1("mohan","Good morning")
f1("Good morning","mohan")

def f1(name,msg):
 print("Hello:",name,msg)
#keyword arguments
f1(name="mohan",msg="Good morning")
f1(msg="Good morning",name="mohan")
#we can use one positional and one keyword
arguments
#but make sure that positional arguments should
#be first then after keyword arguments
f1("mohan",msg="Good morning")
#f1(name="mohan","Good morning") #SyntaxError:
#positional argument follows keyword argument

#3. default arguments

def f1(cource="python"):
 print("course is:",cource)
f1("c")
f1()

#def f1(cource="python",name): #SyntaxError:
#non-default argument follows default argument
def f1(name,cource="python"):
 print(name,"course is:",cource)
f1("sai","c")
f1("mohan")
f1("ram")

#Variable length arguments:
#Ex:
def f1(*a):
 print(a)
f1()
f1(10)
f1(10,20)
f1(10,20,30)
#Ex:
def add(*n):
 s = 0
 for i in n:
     s=s+i

 print("sum is:",s)
add(10,20)
add(2,3,4)
add(2,3,4,5,6,7)
add(10,20,30,40,50,60,70)

#What is *args and **kwargs in python:
#Ex:
def add(*args):
 s = 0
 for i in args:
     s=s+i
 print("sum is:",s)
add(10,20)
add(2,3,4)
add(2,3,4,5,6,7)
add(10,20,30,40,50,60,70)

#**kwargs
#Ex:
def f1(**kwargs):
 print(kwargs)
 for k,v in kwargs.items():
     print(k,"=",v)
f1(a=10,b=20,c=30)
f1(eid=1234,ename="sai",eaddress="hyd",esal=45000)

#Positional only arguments:
def add(a,b,/):
 print("sum is:",a+b)
add(10,20)
#add(a=10,b=20) #TypeError: add() got some
#positional-only a

#Keyword only arguments:
#1.Postional Arguements
def greet(name,msg):
    print("name is",name)
    print("Message is",msg)

greet("Sai","Good Morning")
greet("Good Morning","Ramu") # it is not giving excepted results (postional Arugement)
#2. Keyword Arguemts
greet(msg="Good Morning",name="Rama")  # Key word Arguement

#3. Default Arguements
def student_details(student_name,college="MAllaReddy",streetno="2nd Street",area="Ameerpet",pincode="519007",location="Hyd",collegephonenunber="9898989898"):
    print("Student name is",student_name)
    print("College is",college)
    print("Streetno is",streetno)
    print("Area is",area)
    print("Pincode is",pincode)
    print("Location is",location)
    print("Concat number is",collegephonenunber)

student_details("Rama")
student_details("Sai","SRM","3rd","Sathyabama","500009","Chennai","8989898989")
    

def add(x,y):
    return(x+y)

print("Sum is",add(10,20))

def add(x,y,z):
    return(x+y+z)

print("Sum is",add(10,20,30))

#4. Variable length Arguements
def add(*a):
    print(a)
    print(type(a))
    s=0
    for i in a:
       s=s+i
    return s

print(add(1,2,3,4))
print(add(10,20,30,40,50,60))
print(add(1,2,3,4,5,6,7,8,9,10))


def printdetails(**items):
    print(items)
    print(type(items))
    for i in items.keys():
        print("Key is",i," And Value is ",items[i])

printdetails(a=10,b=20,c=30)
printdetails(empid=210475,ename="Sai",location="Hyd",pincode="500029")








































        





























































                  
    
