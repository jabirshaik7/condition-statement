# 1. Palindrome Number
n = int(input())
print("Palindrome" if str(n) == str(n)[::-1] else "Not Palindrome")

# 2. Sweet Seventeen (Base-17 to Decimal)
s = input().strip()
print(int(s, 17))

# 3. Oddly Even (Digit Position Difference)
num = input().strip()
odd_sum = sum(int(num[i]) for i in range(0,len(num),2))
even_sum = sum(int(num[i]) for i in range(1,len(num),2))
print(abs(odd_sum - even_sum))

# 4. Sum of Primes in Range
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: return False
    return True
l, r = map(int, input().split())
print(sum(i for i in range(l,r+1) if is_prime(i)))

# 5. Reverse Array
n = int(input())
arr = [int(input()) for _ in range(n)]
print(*arr[::-1])

# 6. Push Zeros to End
n = int(input())
arr = [int(input()) for _ in range(n)]
res = [x for x in arr if x != 0] + [0]*(arr.count(0))
print(*res)

# 7. Fibonacci-Prime Interleaved Series
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: return False
    return True
n = int(input())
fib, a, b = [], 0, 1
for _ in range(n):
    fib.append(a); a, b = b, a+b
primes = [i for i in range(2,100) if is_prime(i)]
series = [fib[i] if i%2==0 else primes[i//2] for i in range(n)]
print(*series)

# 8. Ways to Climb Stairs (DP)
n = int(input())
dp = [0]*(n+1); dp[0]=dp[1]=1
for i in range(2,n+1): dp[i]=dp[i-1]+dp[i-2]
print(dp[n])

# 9. Replace Vowels in String
s = input().strip()
print(''.join('#' if ch.lower() in 'aeiou' else ch for ch in s))

# 10. Armstrong Number
n = int(input())
digits = str(n); power = len(digits)
print("Armstrong" if sum(int(d)**power for d in digits)==n else "Not Armstrong")

# 11. Second Largest Unique Element
def second_largest_unique(arr):
    unique = list(set(arr))
    if len(unique) < 2: return None
    unique.sort(reverse=True)
    return unique[1]

print("Second Largest =", second_largest_unique([10,45,32,67,89,23,89,45]))


# 12. Remove Duplicates In-Place (Sorted Array)
def remove_duplicates(nums):
    if not nums: return 0
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

arr = [1,1,2,2,3,4,4,5]
length = remove_duplicates(arr)
print("New length:", length, "Array:", arr[:length])


# 13. Check Anagrams
def are_anagrams(s1, s2):
    from collections import Counter
    return Counter(s1) == Counter(s2)

print("listen/silent:", are_anagrams("listen","silent"))
print("hello/world:", are_anagrams("hello","world"))
