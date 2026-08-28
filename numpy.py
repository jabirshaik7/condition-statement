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
