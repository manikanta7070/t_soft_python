#Accessing tuple elements
print("-------------------------------------")
#1 index : for accessing one elements
#2.slice : for accessing some part of the tuple
print("-------------------------------------")
my_tuple = (1, 2, 3, "apple", "banana")
print(my_tuple[0])  
print(my_tuple[3])  
print(my_tuple[1:4])
print("-------------------------------------")

# Concatenation
new_tuple = my_tuple + ("orange",)
print(new_tuple)  # Output: (1, 2, 3, "apple", "banana", "orange")
print("-------------------------------------")

t=(10,20,-34,23.4,50)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t,4))
print("-------------------------------------")
s="durgasoft"
print(s)
print(type(s))
t=tuple(s)
print(type(t))
print(t)
print("-------------------------------------")
l=[10,20,30,40]
print(l)
print(type(l))
t=tuple(l)
print(t)
print(type(t))

print("-------------------------------------")
#membership operators:
t=(10,20,30)
print(t)
print(type(t))
print(10 in t)
print(100 in t)
print(100 not in t)
print("-------------------------------------")
