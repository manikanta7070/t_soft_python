#while loop
# Generate and print the Fibonacci series up to a given number of terms
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#Check if a given string is a palindrome
word = input("Enter a word: ")
reversed_word = word[::-1]

if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")


#Print the multiplication table of a given number
num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "*", i, "=", num * i)
    i += 1

#Check if a given number is prime

num = int(input("Enter a number: "))
is_prime = True
i = 2

while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#Factorize a given number into its prime factors
    
num = int(input("Enter a number: "))
factor = 2

while num > 1:
    if num % factor == 0:
        print(factor, end=" ")
        num //= factor
    else:
        factor += 1


#Reverse and print a given number

num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed number:", reversed_num)

#Calculate and print the sum of even and odd numbers within a given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
even_sum = 0
odd_sum = 0
num = start

while num <= end:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
    num += 1

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)


#Calculate and print the greatest common divisor of two numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print("GCD:", result)


#Calculate and print the result of raising a number to a given power
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
count = 0

while count < exponent:
    result *= base
    count += 1

print(base, "raised to the power", exponent, "is", result)


#Calculate and print the sum of the digits of a given number

num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print("Sum of digits:", sum_of_digits)




















