#operators
#1.arthemetic operators
print(2+3)
print(4-1)
print(5*2)
print(5**2)
print(5/2)
print(5//2)
print(5%2)

print("----------------------------------------")
#2.relational operators
print(3<4)
print(4>5)
print(4<=4)
print(5>=5)
print(3==3)
print(3!=3)

print("----------------------------------------")
#3.assignment operators

a=5
print(a)
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)
a%=2
print(a)
a**=2
print(a)
print("----------------------------------------")
#logical operators

print(2<3 and 4<5)  
print(2<3 and 4>5)  
print(2<3 or 4>5)
print(2<3 or 1<2)
print(1>2 or 2>3)
print(not(2<3))
print(not(1>2))
print("----------------------------------------")
#membership operators

lst=[2,3,4,5]
print(2 in lst)
print(100 in lst)
print(100 not in lst)
print(2 not in lst)
print("----------------------------------------")
#identity operators

a=2
b=2
print(a is b)
print(a is not b)
a=2
b=3
print(a is b)
print(a is not b)
print("----------------------------------------")
#id() #to find the memory address of varibles or any object
a=2
b=2
print(id(a))
print(id(b))
print(id(a)==id(b))
a=2
b=3
print(id(a))
print(id(b))
a='mohan'
b='Mohan'
print(id(a))
print(id(b))
print(id(a)==id(b))

print("----------------------------------------")
#bitwise operators

a=9
b=5
print(bin(a))
print(bin(b))
print(bin(a&b))
print(a&b)
print(a|b)
print(a^b)
print(~a) 
print(a<<2)
print(a>>2)

print("----------------------------------------")

