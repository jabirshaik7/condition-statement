# 1. Add Two Numbers
a, b = map(int, input("Enter two numbers: ").split())
print("The sum is:", a + b)

# 2. Square a Number
n = int(input("Enter a number: "))
print("The square is:", n ** 2)

# 3. Area of a Circle
import math
r = float(input("Enter radius: "))
print("Area of circle is:", round(math.pi * r * r, 2))

# 4. Greet the User
name = input("Enter your name: ")
print("Hello,", name)

# 5. Convert Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", (c * 9/5) + 32)

# 6. Multiply Three Numbers
a, b, c = map(int, input("Enter three numbers: ").split())
print("Product is:", a * b * c)

# 7. Calculate Simple Interest
p, r, t = map(float, input("Enter Principal, Rate, and Time: ").split())
print("Simple Interest is:", (p * r * t) / 100)

# 8. Find Length of a String
s = input("Enter a string: ")
print("Length of string is:", len(s))

# 9. Append to a List
lst = list(map(int, input("Enter list elements separated by space: ").split()))
x = int(input("Enter element to append: "))
lst.append(x)
print("Updated list:", lst)

# 10. Double Each Element in a List
lst = list(map(int, input("Enter list elements: ").split()))
print("Doubled list:", [i * 2 for i in lst])

# 11. Sort a List
lst = list(map(int, input("Enter list elements: ").split()))
print("Sorted list:", sorted(lst))

# 12. Clear a List Inside Function
def clear_list(lst): lst.clear(); return lst
lst = list(map(int, input("Enter list elements: ").split()))
print("Cleared list:", clear_list(lst))

# 13. Update Dictionary Value
d = {'a': 1}
key = input("Enter key to update: ")
val = int(input("Enter new value: "))
d[key] = val
print("Updated dictionary:", d)

# 14. Remove Element from List by Value
lst = list(map(int, input("Enter list elements: ").split()))
x = int(input("Enter element to remove: "))
lst.remove(x)
print("Updated list:", lst)

# 15. Add Key to Dictionary
d = {'x': 10}
k = input("Enter new key: ")
v = int(input("Enter new value: "))
d[k] = v
print("Updated dictionary:", d)

# 16. Increment All Values in Dictionary
d = {'a': 1, 'b': 2}
d = {k: v + 1 for k, v in d.items()}
print("Updated dictionary:", d)

# 17. Factorial of a Number
n = int(input("Enter a number: "))
print("Factorial is:", math.factorial(n))

# 18. Fibonacci Number (Nth Term)
def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)
n = int(input("Enter term number: "))
print("Fibonacci number is:", fib(n))

# 19. Sum of First N Natural Numbers
n = int(input("Enter a number: "))
print("Sum is:", n * (n + 1) // 2)

# 20. Reverse a String Using Recursion
def reverse(s): return s if len(s) == 0 else reverse(s[1:]) + s[0]
s = input("Enter a string: ")
print("Reversed string is:", reverse(s))

# 21. Power of a Number (Recursion)
def power(a, b): return 1 if b == 0 else a * power(a, b-1)
a, b = map(int, input("Enter base and exponent: ").split())
print("Result is:", power(a, b))

# 22. Sum of Digits Using Recursion
def sum_digits(n): return 0 if n == 0 else n % 10 + sum_digits(n // 10)
n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(n))

# 23. Check Palindrome String Using Recursion
def is_palindrome(s): return True if len(s) <= 1 else s[0] == s[-1] and is_palindrome(s[1:-1])
s = input("Enter a string: ")
print("Is palindrome:", is_palindrome(s))

# 24. GCD of Two Numbers Using Recursion
def gcd(a, b): return a if b == 0 else gcd(b, a % b)
a, b = map(int, input("Enter two numbers: ").split())
print("GCD is:", gcd(a, b))

# 25. Maximum of Three Numbers
a, b, c = map(int, input("Enter three numbers: ").split())
print("Maximum is:", max(a, b, c))

# 26. Sort a List Using sorted()
lst = list(map(int, input("Enter list elements: ").split()))
print("Sorted list:", sorted(lst))

# 27. Sum of Elements Using sum()
lst = list(map(int, input("Enter list elements: ").split()))
print("Sum of list is:", sum(lst))

# 28. Find Data Type Using type()
val = eval(input("Enter any value: "))
print("Data type is:", type(val))

# 29. Print Even Numbers up to N
n = int(input("Enter a number: "))
print("Even numbers:", *[i for i in range(0, n+1, 2)])

# 30. Return List of Squares
lst = list(map(int, input("Enter list elements: ").split()))
print("Squared list:", [i**2 for i in lst])

# 31. Check if Number is Prime
n = int(input("Enter a number: "))
is_prime = all(n % i != 0 for i in range(2, int(n**0.5)+1)) and n > 1
print("Is prime:", is_prime)

# 32. Count Vowels in a String
s = input("Enter a string: ").lower()
print("Number of vowels:", sum(1 for ch in s if ch in "aeiou"))

# 33. Multiply by 2 Using Lambda
n = int(input("Enter a number: "))
print("Result:", (lambda x: x * 2)(n))

# 34. Square List Using map() and Lambda
lst = list(map(int, input("Enter list elements: ").split()))
print("Squared list:", list(map(lambda x: x**2, lst)))

# 35. Filter Even Numbers Using filter() and Lambda
lst = list(map(int, input("Enter list elements: ").split()))
print("Even numbers:", list(filter(lambda x: x % 2 == 0, lst)))

# 36. Sort Tuples by Second Value Using Lambda
lst = [(1, 2), (3, 1)]
print("Sorted list:", sorted(lst, key=lambda x: x[1]))

# 37. Access Global Variable Inside Function
x = "Hello"
def show(): print("Global variable value is:", x)
show()

# 38. Modify Global Variable Inside Function
x = "Hello"
def change():
    global x
    x = "Changed"
    print("Modified global variable is:", x)
change()

# 39. Use Local Variable with Same Name as Global
x = "Global"
def test():
    x = "Local"
    print("Inside function:", x)
test()
print("Outside function:", x)

# 40. Compare Global and Local Variables
x = 10
def compare():
    x = 20
    print("Global x:", globals()['x'])
    print("Local x:", x)
compare()
