#Printing numbers from 1 to N
N = 10
for i in range(1, N+1):
    print(i)

#Calculating the sum of elements in a list
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)

#Finding the factorial of a number
n = 5
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

#Checking for prime numbers within a range
start = 10
end = 50
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)



#Reversing a string using a for loop
word = "Hello"
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(reversed_word)

#Generating a multiplication table
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#Iterating over dictionary keys and values

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

#Drawing patterns using nested for loops
size = 5
for i in range(1, size+1):
    print("*" * i)


#Counting the occurrences of a specific element in a list
numbers = [1, 2, 3, 2, 4, 2, 5]
count = 0
target = 2
for num in numbers:
    if num == target:
        count += 1
print(f"Number of occurrences of {target}: {count}")


# Finding the index of an element in a list

numbers = [10, 20, 30, 40, 50]
target = 30
for index, num in enumerate(numbers):
    if num == target:
        print(f"Element {target} found at index {index}")
        break
else:
    print("Element not found in the list.")





























            
