a=eval(input("Enter a number"))
b=eval(input("Enter 2nd number"))
def add():
    sum= a+b
    print(sum)
add()

def add():    #function definition
    a=eval(input("Enter a number"))
    b=eval(input("Enter 2nd number"))
    c=a+b
    print("Sum is",c)


add() # function calling

# function without arguement and no return type
ef f1():
 for i in range(10):
     print("Hello")

f1()

#functon with paramters and no return type

def square(n):
 print("square is:",n*n)
square(4)

#functon with paramters and return type

def square(n):    
    return (n*n)

result=square(4)

#function without arguements and return type

def Read_values():
    a= eval(input("Enter a number"))
    b= eval(input("Enter 2nd number"))
    return (a,b)
#tuple

t= Read_values()
print(type(t))
print(t[0])
print(t[1])

(x,y)=Read_values()

print("x=",x)
print("y=",y)

def Read_values():
    a= eval(input("Enter a number"))
    b= eval(input("Enter 2nd number"))
    return (a,b)

t= Read_values()
print(type(t))
print(t[0])
print(t[1])

#########

(x,y)=Read_values()

print("x=",x)
print("y=",y)

def max(x,y):
    if x>y:
        return x
    else:
        return y

t= Read_values()

max_value=max(t[0],t[1])

print("max of {} and {} is {}".format(t[0],t[1],max_value))

#sum max min  for list
#sum max min  for tuple
#sum max min  for set

def Read_list_values():
    print("\n Enter how many elements in the list you want")
    n=int(input("Enter value"))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value".format(i))))

    return (l)

def sum_list(l):
    s=0
    for i in l:
        s=s+i
    return s

def max_list(l):
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max

def min_list(l):
    min=l[0]
    for i in l:
        if min>i:
            min=i
    return min
    
list_items=Read_list_values()
sum_of_list_items=sum_list(list_items)


print("Sum of list items is",sum_of_list_items)


max_of_list_items=max_list(list_items)
print("Max of list items is",max_of_list_items)

min_of_list_items=min_list(list_items)
print("Min of list items is",min_of_list_items)













































