
# 1. Print Numbers from 1 to N

N = int(input("Enter N for problem 1: "))
for i in range(1, N + 1):
    print(i)


# 2. Print Even Numbers from 1 to N

N = int(input("Enter N for problem 2: "))
for i in range(2, N + 1, 2):
    print(i)


# 3. Sum of Numbers from 1 to N

N = int(input("Enter N for problem 3: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Sum =", total)


# 4. Print Odd Numbers from 1 to N

N = int(input("Enter N for problem 4: "))
for i in range(1, N + 1, 2):
    print(i)


# 5. Factorial of a Number

N = int(input("Enter N for problem 5: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print("Factorial =", fact)


# 6. Multiplication Table of N

N = int(input("Enter N for problem 6: "))
for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")


# 7. Check Prime Number

N = int(input("Enter N for problem 7: "))
is_prime = True
for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break
print("Prime" if is_prime and N > 1 else "Not Prime")


# 8. Sum of Digits (while loop)

n = int(input("Enter number for problem 8: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digits =", s)


# 9. Fibonacci Sequence up to N terms

N = int(input("Enter N for problem 9: "))
a, b = 0, 1
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()


# 10. Count Numbers Divisible by 3

N = int(input("Enter N for problem 10: "))
count = 0
for i in range(1, N + 1):
    if i % 3 == 0:
        count += 1
print("Count =", count)


# 11. Palindrome Number

n = int(input("Enter number for problem 11: "))
temp, rev = n, 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Palindrome" if rev == n else "Not Palindrome")


# 12. Multiples of 5 up to N

N = int(input("Enter N for problem 12: "))
for i in range(5, N + 1, 5):
    print(i)


# 13. Maximum of Three Numbers

a, b, c = map(int, input("Enter three numbers for problem 13: ").split())
max_num = a
for num in [b, c]:
    if num > max_num:
        max_num = num
print("Maximum =", max_num)


# 14. Reverse of a Number

n = int(input("Enter number for problem 14: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reverse =", rev)


# 15. Sum of First N Natural Numbers

N = int(input("Enter N for problem 15: "))
s = 0
for i in range(1, N + 1):
    s += i
print("Sum =", s)


# 16. Print Numbers from N to 1

N = int(input("Enter N for problem 16: "))
while N > 0:
    print(N)
    N -= 1


# 17. Sum of Prime Numbers up to N

N = int(input("Enter N for problem 17: "))
def is_prime(num):
    if num < 2: return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

total = 0
for i in range(1, N + 1):
    if is_prime(i):
        total += i
print("Sum of primes =", total)


# 18. Product of Digits

n = int(input("Enter number for problem 18: "))
prod = 1
while n > 0:
    prod *= n % 10
    n //= 10
print("Product of digits =", prod)


# 19. Numbers Divisible by Both 3 and 5

N = int(input("Enter N for problem 19: "))
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# 20. GCD of Two Numbers

a, b = map(int, input("Enter two numbers for problem 20: ").split())
while b != 0:
    a, b = b, a % b
print("GCD =", a)


# 21. Right-Angled Triangle Pattern

N = int(input("Enter N for problem 21: "))
for i in range(1, N + 1):
    print("*" * i)


# 22. Hollow Square Pattern

N = int(input("Enter N for problem 22: "))
for i in range(N):
    for j in range(N):
        if i == 0 or i == N-1 or j == 0 or j == N-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 23. Perfect Number

N = int(input("Enter N for problem 23: "))
s = 0
for i in range(1, N):
    if N % i == 0:
        s += i
print("Perfect" if s == N else "Not Perfect")


# 24. Count Digits

n = int(input("Enter number for problem 24: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits =", count)


# 25. Numbers Divisible by 7

N = int(input("Enter N for problem 25: "))
for i in range(7, N + 1, 7):
    print(i)


# 26. LCM of Two Numbers.

a, b = map(int, input("Enter two numbers for problem 26: ").split())
x, y = a, b
while a != b:
    if a < b:
        a += x
    else:
        b += y
print("LCM =", a)


# 27. Even Numbers in Reverse Order

N = int(input("Enter N for problem 27: "))
while N >= 2:
    if N % 2 == 0:
        print(N)
    N -= 1


# 28. Sum of First N Odd Numbers

N = int(input("Enter N for problem 28: "))
s = 0
odd = 1
for i in range(N):
    s += odd
    odd += 2
print("Sum =", s)


# 29. Square Pattern of Numbers

N = int(input("Enter N for problem 29: "))
for i in range(N):
    for j in range(1, N + 1):
        print(j, end=" ")
    print()


# 30. Armstrong Number

n = int(input("Enter number for problem 30: "))
s = 0
digits = len(str(n))
for d in str(n):
    s += int(d) ** digits
print("Armstrong" if s == n else "Not Armstrong")

# control stament questions

# 1. Print prime numbers between 1 and N
N = 50
for num in range(2, N+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

# 2. Find GCD of two numbers using while loop
a, b = 48, 18
while b:
    a, b = b, a % b
print("\nGCD:", a)

# 3. Print pattern of stars in pyramid form
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "*"*(2*i-1))

# 4. Check if a number is perfect (sum of divisors = number)
n = 28
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print("Perfect" if total == n else "Not Perfect")

# 5. Find first 10 numbers divisible by both 3 and 5
count, num = 0, 1
while count < 10:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
        count += 1
    num += 1

# 6. Print Pascal’s Triangle up to N rows
N = 5
for i in range(N):
    val = 1
    print(" "*(N-i), end="")
    for j in range(i+1):
        print(val, end=" ")
        val = val*(i-j)//(j+1)
    print()

# 7. Find sum of digits until single digit (digital root)
n = 9875
while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s
print("Digital Root:", n)

# 8. Print all Armstrong numbers between 100–999
for num in range(100, 1000):
    s = sum(int(d)**3 for d in str(num))
    if s == num:
        print(num, end=" ")

# 9. Generate Collatz sequence for a number
n = 13
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
print(1)

# 10. Find LCM of two numbers using while loop
a, b = 12, 15
x, y = a, b
while a != b:
    if a < b:
        a += x
    else:
        b += y
print("LCM:", a)
