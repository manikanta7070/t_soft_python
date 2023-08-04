<<<<<<< HEAD
#Working with set functions: 
#• Creating a set
s=set()
print(s)
print(type(s))

#add and update methods of set
s={10,20,30,"sai",45.7,10}
print(s)
s.add(33)
print(s)
s.update([44,55,78,"durga"],)
print(s)

#Discard , Remove, Clear methods of set

s={10,20,30,40,50}
print(s)
#s.discard(10)
#s.remove(10)
s1=s.discard(100) #none
print(s1)
#s.remove(100) #KeyError: 100
s.clear()
print(s)


#Deleting a set

s={10,20,30,40,50}
print(s)
del s
print(s) #NameError: name 's' is not define'''

#Set operators : union, intersection, difference, symmetric difference
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A.union(B))

print(A&B)
print(A.intersection(B))

print(A-B)
print(A.difference(B))
print(B-A)


print(A^B)
print(A.symmetric_difference(B))

#Set Len, max, min, sum

s={10,34.5,-45,89,99}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sum(s,9))

#Set membership test

s={10,34.5,-45,89,99}
print(10 in s)
print(9 in s)
print(99 not in s)

#frozensets
vowels = ('a', 'e', 'i', 'o', 'u')
set1 = set(vowels)
print('The set elements are:', set1)
set1.add('v')
print("the set elements are:",set1)
fSet = frozenset(vowels)
print('The fozenset elements are:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
fSet.add('v')  # this statement will throw runtime error
print("the set elements are:",fSet)'''
=======
#Working with set functions: 
#• Creating a set
s=set()
print(s)
print(type(s))

#add and update methods of set
s={10,20,30,"sai",45.7,10}
print(s)
s.add(33)
print(s)
s.update([44,55,78,"durga"],)
print(s)

#Discard , Remove, Clear methods of set

s={10,20,30,40,50}
print(s)
#s.discard(10)
#s.remove(10)
s1=s.discard(100) #none
print(s1)
#s.remove(100) #KeyError: 100
s.clear()
print(s)


#Deleting a set

s={10,20,30,40,50}
print(s)
del s
print(s) #NameError: name 's' is not define'''

#Set operators : union, intersection, difference, symmetric difference
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A.union(B))

print(A&B)
print(A.intersection(B))

print(A-B)
print(A.difference(B))
print(B-A)


print(A^B)
print(A.symmetric_difference(B))

#Set Len, max, min, sum

s={10,34.5,-45,89,99}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sum(s,9))

#Set membership test

s={10,34.5,-45,89,99}
print(10 in s)
print(9 in s)
print(99 not in s)

#frozensets
vowels = ('a', 'e', 'i', 'o', 'u')
set1 = set(vowels)
print('The set elements are:', set1)
set1.add('v')
print("the set elements are:",set1)
fSet = frozenset(vowels)
print('The fozenset elements are:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
fSet.add('v')  # this statement will throw runtime error
print("the set elements are:",fSet)'''
>>>>>>> e8b7454407d53ca75ed19b70c41bdec0b8a86854
