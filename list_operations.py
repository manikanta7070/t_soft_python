#list operations
'''mymarks=["Balaji",78,72,76,98,78,94,"Hyderabad"]
index: mymarks[0]

print("------------------------------------------")

#slicing: [start:end:step]

mymarks[1:7:2]
len(mymarks)
print("------------------------------------------")

mymarks=["Balaji",78,72,76,98,78,94,"Hyderabad"]
print(mymarks)
print(type(mymarks))
print(mymarks[0])
print(mymarks[1:7])

print("------------------------------------------")
mymarks=[78,72,76,98,78,94]
print(max(mymarks))
print(min(mymarks))
print(sum(mymarks))

print("------------------------------------------")
list1=[10,20,30]
list2=[5,15,25]
list3=list1+list2
print(list1)
print(list2)
print(list3)
list4=list1 *2
print(list4)

print("------------------------------------------")
#slicing
s=['h','y','d','e','r','b','a','d']
print(s[2:7])
print(s[:6])
print(s[1:])
print(s[:])
print(s[0:9:1])
print(s[::-1])
print(s[7:1]) #empty string
print(s[-1:-5])
print(s[-5:-1])
print("------------------------------------------")

#nested list:
mymarks=["Balaji",[78,72,76,98,78,94],"Hyderabad"]

print(mymarks[0])
print(mymarks[1])
print(mymarks[2])
print(mymarks[1][5])
print("------------------------------------------")

# Adding  elements to list

l=[2,3,4] #list of 3 elements 
print(l)
l[1]=33# 1 is index and 33 is value
print(l)

print("------------------------------------------")
l=[2,3,4]
print(l)
l.insert(1,33)# 1 is index and 33 is value
print(l)

print("------------------------------------------")
l=[2,3,4]
print(l)
l.append(33)
print(l)

print("------------------------------------------")
l.extend([45,67,89,"sai"])
print(l)

print("------------------------------------------")
# deleting elements from list remove, pop,clear and del

l=[10,20,30,40,50]
print(l)
l.remove(20)
print(l)

print("------------------------------------------")
#l.remove(33) #ValueError: list.remove(x): x not in list
l=[10,20,30,40,50]
print(l)
x=l.pop(2)
print("Removed element is",x)
print(l)
l.clear()
print(l)
del l
print(l)

print("------------------------------------------")

# Sorting

l=[2,6,9,4,3,5,7,1]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

print("------------------------------------------")

#List Copy

l1=[10,20,30,40,50]
print(l1)
l2=l1
print(l2)
l1[1]=200
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l2=l1.copy()
l1[1]=33
print(l1)
print(l2)
print(id(l1))
print(id(l2))

print("------------------------------------------")

# count and index

l=[10,20,30,10,20,10,10,20,10,20]
print(l.count(10))
print(l.count(100))
print(l.index(30))

print("------------------------------------------")






