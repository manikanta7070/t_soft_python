'''#break
#Simple While Loop Break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break

#Break in For Loop
for num in range(10):
    if num == 5:
        break
    print(num)

#Break in Nested Loop
for i in range(3):
   for j in range(3):
        if i + j == 3:
            break
        print(i, j)

#Break in Loop with Else
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed without break.")

#Breaking on Condition
numbers = [2, 4, 6, 8, 10, 12]
for num in numbers:
    if num % 3 == 0:
        break
    print(num)

#Breaking from While Loop based on User Input

while True:
    user_input = input("Enter 'exit' to break: ")
    if user_input == 'exit':
        break


#Using Break with List Comprehension
numbers = [1, 2, 3, 4, 5, 6]
result = [num for num in numbers if num > 3]
print(result)

#Breaking from Nested Loop with a Flag

found = False
for i in range(5):
    for j in range(5):
        if i * j > 6:
            found = True
            break
    if found:
        break

#Breaking from Loop with a Function

def check_condition(value):
    return value > 7

numbers = [5, 8, 3, 9, 2]
for num in numbers:
    if check_condition(num):
        break


#Breaking from Loop in Exception Handling

try:
    for i in range(10):
        if i == 7:
            raise Exception("Encountered a critical value.")
except Exception as e:
    print(e)

#continue

#Skipping Odd Numbers

for num in range(1, 11):
    if num % 2 == 1:
        continue
    print(num)

#Skipping Specific Values
    
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
for num in numbers:
    if num < 5:
        continue
    print(num)
#Skipping Vowels in a String
    
word = "hello"
for letter in word:
    if letter in "aeiou":
        continue
    print(letter)
    
#Skipping Iteration in Nested Loop

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)
        
#Skipping Negative Numbers

numbers = [-2, 3, -5, 6, -8, 10]
for num in numbers:
    if num < 0:
        continue
    print(num)
#Skipping Iteration in While Loop
    
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
#Skipping Iteration Based on Function

def should_skip(value):
    return value % 3 == 0

for i in range(1, 11):
    if should_skip(i):
        continue
    print(i)
#Skipping Even-Length Words
    
words = ["apple", "banana", "cherry", "date", "elderberry"]
for word in words:
    if len(word) % 2 == 0:
        continue
    print(word)
#Skipping Characters in a String:

sentence = "Python is a great programming language."
for char in sentence:
    if char == ' ':
        continue
    print(char)
#Skipping Values with Specific Property
    
numbers = [15, 23, 8, 14, 30, 47, 62]
for num in numbers:
    if num % 5 == 0:
        continue
    print(num)


#programs on pass statement

#Empty Function
    
def my_function():
    pass
#Empty Class:

class EmptyClass:
    pass

#Stubbing Out Functions:

def process_data(data):
    if not data:
        pass
    # Continue with data processing
    
#Placeholder Loop
for item in my_list:
    # Perform some checks
    if not condition_met(item):
        pass
    # Continue processing other items
#Incomplete Conditional
if user_input == 'admin':
    pass  # Handle admin functionality later
else:
    # Handle regular user functionality
    
#Placeholders in Classes
 class MyIncompleteClass:
    def method1(self):
        pass
    
    def method2(self):
        pass
#Using Pass in Exception Handling
try:
    perform_operation()
except SomeError:
    pass  # Handle the error case later
#Creating a Placeholder Block
def my_function():
    pass
    # TODO: Add actual implementation
    
#Creating Empty Control Structures
if condition:
    pass  # Implement condition later

while some_condition:
    pass  # Implement loop later'''

#Creating a Placeholder in a Loop

for item in my_list:
    if not is_valid(item):
        pass  # Handle invalid items later
    process(item)



























