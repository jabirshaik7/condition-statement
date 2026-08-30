#1. Divisible by 3 AND 5
import numpy as np
a=np.array([10,15,20,30,45,50,60,75])
print(a[(a%3==0)&(a%5==0)])

#2. Divisible by 2 OR 7
a=np.array([7,10,14,15,20,21,25,28])
print(a[(a%2==0)|(a%7==0)])

#3. Between 20 and 60
a=np.array([10,25,35,50,60,75])
print(a[(a>20)&(a<60)])

#4. Positive even OR negative odd
a=np.array([-9,-6,-3,2,4,7,10,13])
print(a[((a>0)&(a%2==0))|((a<0)&(a%2!=0))])

#5. Second-largest unique number
a=np.array([10,50,20,50,40,30,40,60])
print(np.unique(a)[-2])

#6. Replace negative numbers with 0
a=np.array([-5,10,-2,20,-8,30])
print(np.where(a>0,a,0))

#7. Even AND greater than average
a=np.array([10,15,20,25,30,40])
avg=np.mean(a)
print(a[(a%2==0)&(a>avg)])

#8. NOT divisible by 3
a=np.array([3,7,10,12,14,18,20,25])
print(a[~(a%3==0)])

#9. Largest positive number
a=np.array([-20,15,-5,40,10,-2,35])
print(np.max(a[a>0]))

#10. Multiple conditions

#Positive & even OR greater than 50 & divisible by 5

a=np.array([-10,12,15,20,35,50,55,60,75,81])
c=((a>0)&(a%2==0))|((a>50)&(a%5==0))
print(a[c])


#1. Find numbers divisible by 3 AND 5 using NumPy
import numpy as np

a = np.array([10, 15, 20, 30, 45, 50, 60, 75])

result = a[(a % 3 == 0) & (a % 5 == 0)]

print(result)


#2. Find numbers divisible by 2 OR 7
import numpy as np

a = np.array([7, 10, 14, 15, 20, 21, 25, 28])

result = a[(a % 2 == 0) | (a % 7 == 0)]

print(result)


#3. Find numbers greater than 20 AND less than 60
import numpy as np

a = np.array([10, 25, 35, 50, 60, 75])

result = a[(a > 20) & (a < 60)]

print(result)


#4. Find positive even numbers and negative odd numbers
import numpy as np

a = np.array([-9, -6, -3, 2, 4, 7, 10, 13])

result = a[((a > 0) & (a % 2 == 0)) |
           ((a < 0) & (a % 2 != 0))]

print(result)


#5. Find the second-largest unique number
import numpy as np

a = np.array([10, 50, 20, 50, 40, 30, 40, 60])

unique = np.unique(a)
result = unique[-2]

print(result)


#6. Replace negative numbers with 0 and keep positive numbers
import numpy as np

a = np.array([-5, 10, -2, 20, -8, 30])

result = np.where(a > 0, a, 0)


#7. Find elements that are even AND greater than the array average
import numpy as np

a = np.array([10, 15, 20, 25, 30, 40])

average = np.mean(a)

result = a[(a % 2 == 0) & (a > average)]

print("Average:", average)
print("Result:", result)


#8. Find numbers that are NOT divisible by 3
import numpy as np

a = np.array([3, 7, 10, 12, 14, 18, 20, 25])

result = a[~(a % 3 == 0)]

print(result)



#9. Find the largest number among positive numbers only
import numpy as np

a = np.array([-20, 15, -5, 40, 10, -2, 35])

positive = a[a > 0]

if len(positive) > 0:
    print(np.max(positive))
else:
    print("No positive numbers")


#10.Find numbers satisfying multiple conditions

#Condition: Number must be positive AND even, OR it must be greater than 50 AND divisible by 5.

import numpy as np

a = np.array([-10, 12, 15, 20, 35, 50, 55, 60, 75, 81])

condition = ((a > 0) & (a % 2 == 0)) | \
            ((a > 50) & (a % 5 == 0))

result = a[condition]

print(result)


# 1. Find all prime numbers in a NumPy array
a = np.array([10, 11, 12, 13, 14, 15, 16, 17])
is_prime = np.vectorize(lambda x: all(x % np.arange(2, int(np.sqrt(x))+1) != 0) and x > 1)
print(a[is_prime(a)])   # [11 13 17]

# 2. Replace all odd numbers with -1 without using loops
a = np.arange(1, 11)
a[a % 2 == 1] = -1
print(a)   # [-1 2 -1 4 -1 6 -1 8 -1 10]

# 3. Create a 5x5 matrix with row values increasing from 0 to 4
print(np.tile(np.arange(5), (5,1)))

# 4. Normalize a random vector (make its magnitude = 1)
v = np.random.rand(5)
v = v / np.linalg.norm(v)
print(v)

# 5. Find common elements between two arrays
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])
print(np.intersect1d(a,b))   # [4 5]

# 6. Generate a checkerboard pattern (8x8)
print(np.indices((8,8)).sum(axis=0) % 2)

# 7. Find the most frequent value in an array
a = np.random.randint(0, 10, 20)
vals, counts = np.unique(a, return_counts=True)
print(vals[np.argmax(counts)])

# 8. Multiply two matrices and check if result is symmetric
A = np.random.randint(1,5,(3,3))
B = np.random.randint(1,5,(3,3))
C = A @ B
print(np.allclose(C, C.T))

# 9. Replace maximum value in each row with 0
a = np.random.randint(1,100,(5,5))
a[np.arange(5), np.argmax(a, axis=1)] = 0
print(a)

# 10. Compute pairwise Euclidean distances between points
points = np.random.rand(5,2)
dist = np.sqrt(((points[:,None,:] - points[None,:,:])**2).sum(axis=2))
print(dist)

# 1. Reverse words in a sentence without using split()
s = "Python is powerful"
print(" ".join(s[::-1].split()[::-1]))   # "powerful is Python"

# 2. Find all anagrams in a list of words
words = ["listen","silent","enlist","rat","tar","art"]
from collections import defaultdict
d = defaultdict(list)
for w in words: d["".join(sorted(w))].append(w)
print([v for v in d.values() if len(v)>1])  # [['listen','silent','enlist'], ['rat','tar','art']]

# 3. Flatten a nested list without recursion
nested = [[1,2],[3,[4,5]],6]
from collections.abc import Iterable
def flatten(lst):
    stack, out = [iter(lst)], []
    while stack:
        for x in stack[-1]:
            if isinstance(x, Iterable) and not isinstance(x, (str,bytes)):
                stack.append(iter(x)); break
            else: out.append(x)
        else: stack.pop()
    return out
print(flatten(nested))   # [1,2,3,4,5,6]

# 4. Find the longest substring without repeating characters
s = "abcabcbb"
seen, start, maxlen = {}, 0, 0
for i,ch in enumerate(s):
    if ch in seen and seen[ch]>=start: start = seen[ch]+1
    seen[ch] = i
    maxlen = max(maxlen, i-start+1)
print(maxlen)   # 3 ("abc")

# 5. Implement a decorator to time function execution
import time
def timer(func):
    def wrapper(*args,**kwargs):
        t0=time.time(); result=func(*args,**kwargs)
        print("Time:",time.time()-t0); return result
    return wrapper
@timer
def slow(): sum(i*i for i in range(10**6))
slow()

# 6. Find pairs in list that sum to target using set
nums=[2,7,11,15]; target=9
seen=set()
for n in nums:
    if target-n in seen: print((n,target-n))
    seen.add(n)   # (7,2)

# 7. Rotate a matrix 90° clockwise
mat=[[1,2,3],[4,5,6],[7,8,9]]
rot=list(zip(*mat[::-1]))
print(rot)   # [(7,4,1),(8,5,2),(9,6,3)]

# 8. Generate Pascal’s Triangle up to n rows
def pascal(n):
    tri=[[1]]
    for _ in range(n-1):
        tri.append([1]+[tri[-1][i]+tri[-1][i+1] for i in range(len(tri[-1])-1)]+[1])
    return tri
print(pascal(5))

# 9. LRU Cache implementation using OrderedDict
from collections import OrderedDict
class LRU:
    def __init__(self,cap): self.cap=cap; self.cache=OrderedDict()
    def get(self,k): return self.cache.get(k,-1)
    def put(self,k,v):
        if k in self.cache: self.cache.move_to_end(k)
        self.cache[k]=v
        if len(self.cache)>self.cap: self.cache.popitem(last=False)
l=LRU(2); l.put(1,1); l.put(2,2); l.put(3,3)
print(l.cache)   # {2:2,3:3}

# 10. Detect palindrome ignoring non-alphanumeric
import re
s="A man, a plan, a canal: Panama"
clean=re.sub(r'[^a-z0-9]','',s.lower())
print(clean==clean[::-1])   # True

# 1. Find the kth largest element in a list without sorting
import heapq
nums=[3,2,1,5,6,4]; k=2
print(heapq.nlargest(k,nums)[-1])   # 5

# 2. Generate all permutations of a string
from itertools import permutations
s="abc"
print([''.join(p) for p in permutations(s)])  # ['abc','acb','bac','bca','cab','cba']

# 3. Implement binary search recursively
def bsearch(arr,x,l=0,r=None):
    r=len(arr)-1 if r is None else r
    if l>r: return -1
    mid=(l+r)//2
    if arr[mid]==x: return mid
    return bsearch(arr,x,l,mid-1) if x<arr[mid] else bsearch(arr,x,mid+1,r)
print(bsearch([1,2,3,4,5],4))   # 3

# 4. Detect cycle in a linked list
class Node:
    def __init__(self,v): self.v=v; self.next=None
a=Node(1); b=Node(2); c=Node(3)
a.next=b; b.next=c; c.next=a
slow=fast=a
while fast and fast.next:
    slow=slow.next; fast=fast.next.next
    if slow==fast: print("Cycle detected"); break

# 5. Find longest palindrome substring
s="babad"
def longest_pal(s):
    res=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub=s[i:j+1]
            if sub==sub[::-1] and len(sub)>len(res): res=sub
    return res
print(longest_pal(s))   # "bab" or "aba"

# 6. Implement quicksort
def quicksort(arr):
    if len(arr)<=1: return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+mid+quicksort(right)
print(quicksort([3,6,8,10,1,2,1]))

# 7. Find missing number in array 1..n
arr=[1,2,4,5]
n=5
print(n*(n+1)//2 - sum(arr))   # 3

# 8. Implement Fibonacci with memoization
from functools import lru_cache
@lru_cache(None)
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
print(fib(10))   # 55

# 9. Count frequency of characters in a string
s="programming"
from collections import Counter
print(Counter(s))   # {'r':2,'g':2,'m':2,'p':1,'o':1,'a':1,'i':1,'n':1}

# 10. Solve Tower of Hanoi
def hanoi(n,src,dst,aux):
    if n==1: print(f"Move disk 1 from {src} to {dst}"); return
    hanoi(n-1,src,aux,dst)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n-1,aux,dst,src)
hanoi(3,'A','C','B')

