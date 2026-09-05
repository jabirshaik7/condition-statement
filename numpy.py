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

# 1. Find all subsets of a set (power set)
from itertools import chain, combinations
s = {1,2,3}
print(list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1))))
# [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]

# 2. Implement matrix transpose without NumPy
mat = [[1,2,3],[4,5,6],[7,8,9]]
print([[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))])

# 3. Find longest common prefix among strings
words = ["flower","flow","flight"]
prefix = ""
for i in zip(*words):
    if len(set(i))==1: prefix += i[0]
    else: break
print(prefix)   # "fl"

# 4. Detect balanced parentheses
s = "{[()]}"
stack, pairs = [], {')':'(',']':'[','}':'{'}
ok=True
for ch in s:
    if ch in pairs.values(): stack.append(ch)
    elif ch in pairs and (not stack or stack.pop()!=pairs[ch]): ok=False; break
print(ok)   # True

# 5. Find majority element (> n/2 times)
nums=[2,2,1,1,1,2,2]
count, candidate=0,None
for n in nums:
    if count==0: candidate=n
    count += (1 if n==candidate else -1)
print(candidate)   # 2

# 6. Generate spiral matrix n x n
n=3; mat=[[0]*n for _ in range(n)]
val=1; l,r,t,b=0,n-1,0,n-1
while l<=r and t<=b:
    for i in range(l,r+1): mat[t][i]=val; val+=1
    t+=1
    for i in range(t,b+1): mat[i][r]=val; val+=1
    r-=1
    for i in range(r,l-1,-1): mat[b][i]=val; val+=1
    b-=1
    for i in range(b,t-1,-1): mat[i][l]=val; val+=1
    l+=1
print(mat)

# 7. Find longest increasing subsequence (DP)
arr=[10,9,2,5,3,7,101,18]
dp=[1]*len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i]>arr[j]: dp[i]=max(dp[i],dp[j]+1)
print(max(dp))   # 4

# 8. Implement merge intervals
intervals=[[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x:x[0])
merged=[intervals[0]]
for s,e in intervals[1:]:
    if s<=merged[-1][1]: merged[-1][1]=max(merged[-1][1],e)
    else: merged.append([s,e])
print(merged)   # [[1,6],[8,10],[15,18]]

# 9. Find first non-repeating character in string
s="swiss"
from collections import Counter
cnt=Counter(s)
print(next(ch for ch in s if cnt[ch]==1))   # 'w'

# 10. Implement binary tree level order traversal
from collections import deque
class Node:
    def __init__(self,v): self.v=v; self.left=self.right=None
root=Node(1); root.left=Node(2); root.right=Node(3); root.left.left=Node(4)
q=deque([root]); res=[]
while q:
    node=q.popleft(); res.append(node.v)
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)
print(res)   # [1,2,3,4]

# 1. Find the median of two sorted arrays (merge approach)
a=[1,3]; b=[2]
merged=sorted(a+b)
n=len(merged)
median=(merged[n//2] if n%2 else (merged[n//2-1]+merged[n//2])/2)
print(median)   # 2

# 2. Implement string pattern matching (KMP algorithm)
def kmp_search(text,pat):
    lps=[0]*len(pat); j=0
    for i in range(1,len(pat)):
        while j>0 and pat[i]!=pat[j]: j=lps[j-1]
        if pat[i]==pat[j]: j+=1; lps[i]=j
    res=[]; j=0
    for i in range(len(text)):
        while j>0 and text[i]!=pat[j]: j=lps[j-1]
        if text[i]==pat[j]: j+=1
        if j==len(pat): res.append(i-j+1); j=lps[j-1]
    return res
print(kmp_search("ababcabcabababd","ababd"))   # [10]

# 3. Find maximum subarray sum (Kadane’s Algorithm)
arr=[-2,1,-3,4,-1,2,1,-5,4]
max_sum=cur=arr[0]
for x in arr[1:]:
    cur=max(x,cur+x); max_sum=max(max_sum,cur)
print(max_sum)   # 6

# 4. Serialize and deserialize a binary tree
import json
class Node:
    def __init__(self,v): self.v=v; self.left=self.right=None
root=Node(1); root.left=Node(2); root.right=Node(3)
def serialize(node):
    if not node: return None
    return {"v":node.v,"left":serialize(node.left),"right":serialize(node.right)}
def deserialize(d):
    if not d: return None
    n=Node(d["v"]); n.left=deserialize(d["left"]); n.right=deserialize(d["right"]); return n
data=json.dumps(serialize(root))
print(data)

# 5. Find shortest path in graph (Dijkstra)
import heapq
graph={0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]}
dist={0:0}; pq=[(0,0)]
while pq:
    d,u=heapq.heappop(pq)
    if d>dist[u]: continue
    for v,w in graph[u]:
        if v not in dist or d+w<dist[v]:
            dist[v]=d+w; heapq.heappush(pq,(dist[v],v))
print(dist)   # {0:0,2:1,1:3,3:4}

# 6. Find longest consecutive sequence in array
nums=[100,4,200,1,3,2]
s=set(nums); longest=0
for n in s:
    if n-1 not in s:
        length=1
        while n+length in s: length+=1
        longest=max(longest,length)
print(longest)   # 4

# 7. Implement LCS (Longest Common Subsequence)
X="AGGTAB"; Y="GXTXAYB"
dp=[[0]*(len(Y)+1) for _ in range(len(X)+1)]
for i in range(1,len(X)+1):
    for j in range(1,len(Y)+1):
        dp[i][j]=dp[i-1][j-1]+1 if X[i-1]==Y[j-1] else max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])   # 4

# 8. Find top k frequent elements
nums=[1,1,1,2,2,3]; k=2
from collections import Counter
print([x for x,_ in Counter(nums).most_common(k)])   # [1,2]

# 9. Implement matrix multiplication manually
A=[[1,2],[3,4]]; B=[[2,0],[1,2]]
res=[[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print(res)   # [[4,4],[10,8]]

# 10. Solve N-Queens problem (backtracking)
def solveNQueens(n):
    res=[]; cols=set(); diag1=set(); diag2=set()
    def backtrack(r,board):
        if r==n: res.append(["".join(row) for row in board]); return
        for c in range(n):
            if c in cols or r-c in diag1 or r+c in diag2: continue
            board[r][c]='Q'; cols.add(c); diag1.add(r-c); diag2.add(r+c)
            backtrack(r+1,board)
            board[r][c]='.'; cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)
    backtrack(0,[['.']*n for _ in range(n)])
    return res
print(solveNQueens(4))

# 1. Find median of a stream of numbers using two heaps
import heapq
low, high = [], []
def add_num(num):
    heapq.heappush(low, -num)
    heapq.heappush(high, -heapq.heappop(low))
    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))
def median():
    return (-low[0] if len(low)>len(high) else (-low[0]+high[0])/2)
for n in [5,15,1,3]:
    add_num(n); print(median())
# Output: 5,10,5,4

# 2. Implement Trie and search prefix
class Trie:
    def __init__(self): self.children={}; self.end=False
    def insert(self,w):
        node=self
        for ch in w: node=node.children.setdefault(ch,Trie())
        node.end=True
    def startsWith(self,p):
        node=self
        for ch in p:
            if ch not in node.children: return False
            node=node.children[ch]
        return True
t=Trie(); t.insert("apple")
print(t.startsWith("app"))   # True

# 3. Find maximum product subarray
arr=[2,3,-2,4]
cur_max=cur_min=res=arr[0]
for x in arr[1:]:
    cur_max,cur_min=max(x,cur_max*x,cur_min*x),min(x,cur_max*x,cur_min*x)
    res=max(res,cur_max)
print(res)   # 6

# 4. Word ladder shortest transformation
from collections import deque
begin,end="hit","cog"
wordList={"hot","dot","dog","lot","log","cog"}
q=deque([(begin,1)])
while q:
    w,d=q.popleft()
    if w==end: print(d); break
    for i in range(len(w)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            nxt=w[:i]+c+w[i+1:]
            if nxt in wordList:
                wordList.remove(nxt); q.append((nxt,d+1))
# Output: 5

# 5. Find maximum rectangle in histogram
heights=[2,1,5,6,2,3]
stack=[]; max_area=0
for i,h in enumerate(heights+[0]):
    while stack and heights[stack[-1]]>h:
        H=heights[stack.pop()]
        W=i if not stack else i-stack[-1]-1
        max_area=max(max_area,H*W)
    stack.append(i)
print(max_area)   # 10

# 6. Sudoku solver (backtracking)
board=[["5","3",".",".","7",".",".",".","."], ...] # shortened
def valid(b,r,c,ch):
    for i in range(9):
        if b[r][i]==ch or b[i][c]==ch or b[r//3*3+i//3][c//3*3+i%3]==ch: return False
    return True
def solve(b):
    for r in range(9):
        for c in range(9):
            if b[r][c]==".":
                for ch in "123456789":
                    if valid(b,r,c,ch):
                        b[r][c]=ch
                        if solve(b): return True
                        b[r][c]="."
                return False
    return True

# 7. Find kth smallest element in BST
class Node:
    def __init__(self,v): self.v=v; self.left=self.right=None
root=Node(5); root.left=Node(3); root.right=Node(6); root.left.left=Node(2); root.left.right=Node(4)
def inorder(node):
    return inorder(node.left)+[node.v]+inorder(node.right) if node else []
print(inorder(root)[2])   # 4 (3rd smallest)

# 8. Detect duplicate subtrees in binary tree
seen=set(); res=[]
def serialize(node):
    if not node: return "#"
    s=f"{node.v},{serialize(node.left)},{serialize(node.right)}"
    if s in seen: res.append(node.v)
    seen.add(s); return s

# 9. Implement producer-consumer with threading
import threading,queue,time
q=queue.Queue()
def producer():
    for i in range(5): q.put(i); time.sleep(0.1)
def consumer():
    while True:
        item=q.get(); print("Consumed",item)
        if item==4: break
threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()

# 10. Find shortest palindrome by adding chars in front
s="aacecaaa"
rev=s[::-1]
for i in range(len(s)):
    if s.startswith(rev[i:]): 
        print(rev[:i]+s); break
# Output: "aaacecaaa"

# 1. Find maximum sum rectangle in a 2D matrix
mat=[[1,2,-1,-4,-20],[ -8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
import sys
def max_sum_rectangle(matrix):
    R,C=len(matrix),len(matrix[0]); max_sum=-sys.maxsize
    for left in range(C):
        temp=[0]*R
        for right in range(left,C):
            for i in range(R): temp[i]+=matrix[i][right]
            cur_sum=0; best=-sys.maxsize
            for x in temp:
                cur_sum=max(x,cur_sum+x); best=max(best,cur_sum)
            max_sum=max(max_sum,best)
    return max_sum
print(max_sum_rectangle(mat))   # 29

# 2. Implement LFU Cache
from collections import defaultdict,OrderedDict
class LFU:
    def __init__(self,cap): self.cap=cap; self.data={}; self.freq=defaultdict(OrderedDict); self.minf=0
    def get(self,k):
        if k not in self.data: return -1
        v,f=self.data[k]; del self.freq[f][k]
        if not self.freq[f] and f==self.minf: self.minf+=1
        self.freq[f+1][k]=v; self.data[k]=(v,f+1); return v
    def put(self,k,v):
        if self.cap==0: return
        if k in self.data: self.data[k]=(v,self.data[k][1]); self.get(k); return
        if len(self.data)==self.cap:
            kk,_=self.freq[self.minf].popitem(last=False); del self.data[kk]
        self.freq[1][k]=v; self.data[k]=(v,1); self.minf=1

# 3. Find longest repeating subsequence
s="aabb"
n=len(s); dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if s[i-1]==s[j-1] and i!=j: dp[i][j]=1+dp[i-1][j-1]
        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][n])   # 2 ("aa" or "bb")

# 4. Implement Min Stack
class MinStack:
    def __init__(self): self.stack=[]; self.min=[]
    def push(self,x): self.stack.append(x); self.min.append(x if not self.min else min(x,self.min[-1]))
    def pop(self): self.stack.pop(); self.min.pop()
    def top(self): return self.stack[-1]
    def getMin(self): return self.min[-1]

# 5. Find maximum path sum in binary tree
class Node:
    def __init__(self,v): self.v=v; self.left=self.right=None
root=Node(-10); root.left=Node(9); root.right=Node(20); root.right.left=Node(15); root.right.right=Node(7)
max_sum=-sys.maxsize
def dfs(node):
    global max_sum
    if not node: return 0
    l=max(dfs(node.left),0); r=max(dfs(node.right),0)
    max_sum=max(max_sum,node.v+l+r)
    return node.v+max(l,r)
dfs(root); print(max_sum)   # 42

# 6. Implement word break problem
s="leetcode"; wordDict={"leet","code"}
dp=[False]*(len(s)+1); dp[0]=True
for i in range(1,len(s)+1):
    for w in wordDict:
        if dp[i-len(w)] and s[i-len(w):i]==w: dp[i]=True
print(dp[-1])   # True

# 7. Find minimum window substring
s,t="ADOBECODEBANC","ABC"
from collections import Counter
need=Counter(t); missing=len(t); i=start=end=0
for j,ch in enumerate(s,1):
    if need[ch]>0: missing-=1
    need[ch]-=1
    if missing==0:
        while i<j and need[s[i]]<0: need[s[i]]+=1; i+=1
        if end==0 or j-i<end-start: start,end=i,j
print(s[start:end])   # "BANC"

# 8. Implement topological sort (Kahn’s Algorithm)
graph={5:[2,0],4:[0,1],2:[3],3:[1],1:[],0:[]}
indegree={u:0 for u in graph}
for u in graph:
    for v in graph[u]: indegree[v]+=1
q=[u for u in graph if indegree[u]==0]; res=[]
while q:
    u=q.pop(0); res.append(u)
    for v in graph[u]:
        indegree[v]-=1
        if indegree[v]==0: q.append(v)
print(res)   # [5,4,2,3,1,0]

# 9. Implement regex matching ('.' and '*')
def isMatch(s,p):
    dp=[[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0]=True
    for j in range(2,len(p)+1):
        if p[j-1]=="*": dp[0][j]=dp[0][j-2]
    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            if p[j-1]==s[i-1] or p[j-1]==".":
                dp[i][j]=dp[i-1][j-1]
            elif p[j-1]=="*":
                dp[i][j]=dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=="."))
    return dp[-1][-1]
print(isMatch("aab","c*a*b"))   # True

# 10. Implement coin change (minimum coins)
coins=[1,2,5]; amount=11
dp=[amount+1]*(amount+1); dp[0]=0
for c in coins:
    for x in range(c,amount+1):
        dp[x]=min(dp[x],dp[x-c]+1)
print(dp[amount])   # 3 (11=5+5+1)
