# 1. Positive or Negative
num = 5
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 2. Even or Odd
num = 8
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. Divisible by 5
num = 15
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 4. Divisible by 3 and 7
num = 21
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both")

# 5. Leap Year
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

#Divisible by 400 → leap year

#Divisible by 100 but not 400 → not leap year

#Divisible by 4 but not 100 → leap year

# 6. Pass or Fail
marks = 40
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 7. 3-digit number
num = 123
if 100 <= num <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")

#Condition: 100 <= num <= 999

#This is a chained comparison in Python.

#It checks if num is greater than or equal to 100 AND less than or equal to 999 at the same time.

#So it’s basically saying: “Is num between 100 and 999 inclusive?”    

# 8. Vowel check
ch = 'a'
if ch.lower() in ['a','e','i','o','u']:
    print("Vowel")
else:
    print("Consonant")

# 9. Greatest of two numbers
a, b = 7, 9
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

#⚡ Without f-string
# If you didn’t use f, you’d have to write: 
# print(str(a) + " is greater")

a, b = 88, 98
if a > b:
    print(str(a) + " is greater")
else:
    print(str(b) + " is greater")

# 10. Smallest of two numbers
a, b = 3, 8
if a < b:
    print(f"{a} is smaller")
else:
    print(f"{b} is smaller")

# 11. Check if number is zero
num = 0
if num == 0:
    print("Number is zero")
else:
    print("Number is not zero")

#Condition: if num == 0:
#Here, == is the comparison operator (called the equality operator).

# 12. Multiple of 10
num = 50
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")

# 13. Eligible to vote
age = 19
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 14. Number between 1 and 100
num = 45
if 1 <= num <= 100:
    print("In range")
else:
    print("Out of range")

# 15. Square check
x, y = 4, 2
if x == y**2:
    print(f"{x} is square of {y}")
else:
    print("Not a square")

# 16. Strings equal
s1, s2 = "apple", "apple"
if s1 == s2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# 17. Prime number (basic logic)
num = 7
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# 18. Positive and Even
num = 12
if num > 0 and num % 2 == 0:
    print("Positive and even number")
else:
    print("Condition not met")

# 19. Uppercase check
ch = 'A'
if ch.isupper():
    print("Uppercase letter")
else:
    print("Not uppercase")

# 20. Temperature hot check
temp = 35
if temp > 30:
    print("It's hot")
else:
    print("It's not hot")

###----condition statements-----###

# 1. Check if a number is a 4-digit even number
num = 2468
if 1000 <= num <= 9999 and num % 2 == 0:
    print("4-digit even number")
else:
    print("Not a 4-digit even number")

# 2. Check if a character is a consonant
ch = "b"
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 3. Divisible by 2 or 3 but not both
num = 6
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2 only")
elif num % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Not divisible by 2 or 3")

# 4. Negative and odd
num = -5
if num < 0 and num % 2 != 0:
    print("Negative and odd number")

# 5. String starts with a vowel
s = "apple"
if s[0].lower() in "aeiou":
    print("Starts with a vowel")
else:
    print("Does not start with a vowel")

# 6. Valid triangle check
a, b, c = 3, 4, 5
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")

# 7. Greatest among three numbers
a, b, c = 12, 45, 30
print(max(a, b, c), "is the greatest")

# 8. Century year and leap year
year = 2000
if year % 100 == 0 and (year % 400 == 0):
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not leap year")
else:
    print("Not a century year")

# 9. Character is a digit
ch = "5"
if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")

# 10. Palindrome number
num = 121
if str(num) == str(num)[::-1]:
    print("Palindrome number")
else:
    print("Not palindrome")

# 11. Compare lengths of two strings
s1, s2 = "cat", "mouse"
if len(s1) > len(s2):
    print("First string is longer")
elif len(s1) < len(s2):
    print("Second string is longer")
else:
    print("Both strings are equal length")

# 12. Number in range 50–100 and divisible by 5
num = 75
if 50 <= num <= 100 and num % 5 == 0:
    print("In range and divisible by 5")
else:
    print("Condition not met")

# 13. Strong password length
password = "secure123"
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# 14. Sum of two numbers is even
a, b = 12, 16
if (a+b) % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")

# 15. Special character check
ch = "@"
if ch in "!@#$%^&*()":
    print("Special character")
else:
    print("Not a special character")

# 16. Temperature check
temp = 10
if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Moderate")
else:
    print("Hot")

# 17. Number outside range 10–50
num = 55
if num < 10 or num > 50:
    print("Outside the range")
else:
    print("Within the range")

# 18. Perfect square check
num = 36
if int(num**0.5)**2 == num:
    print("Perfect square")
else:
    print("Not a perfect square")

# 19. Compare two ages
age1, age2 = 22, 25
if age1 > age2:
    print("First person is older")
elif age1 < age2:
    print("Second person is older")
else:
    print("Both are same age")

# 20. Angle type
angle = 90
if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
else:
    print("Obtuse angle")

