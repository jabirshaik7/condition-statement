# 1. Triangle type
a, b, c = 5, 5, 8
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# 2. Character classification
ch = '@'
if ch.lower() in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# 3. BMI Calculator
height, weight = 1.65, 72
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 4. Electricity bill
units = 250
bill = 0
if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100*1 + (units-100)*2
else:
    bill = 100*1 + 100*2 + (units-200)*3
print("₹", bill)

# 5. Armstrong number
num = 153
s = sum(int(d)**3 for d in str(num))
print("Armstrong" if s == num else "Not Armstrong")

# 6. Strong password
pwd = "Abcdef@1"
if (len(pwd) >= 8 and any(ch.isupper() for ch in pwd) and
    any(ch.isdigit() for ch in pwd) and
    any(ch in "!@#$%^&*()" for ch in pwd)):
    print("Strong Password")
else:
    print("Weak Password")

# 7. ATM Withdrawal
balance, withdraw = 2000, 700
if withdraw >= 500 and withdraw % 100 == 0 and withdraw <= balance:
    print("Success")
else:
    print("Insufficient Balance")

# 8. Ticket fare
age = 65
fare = 100
if age < 5:
    fare = 0
elif age < 18:
    fare = fare * 0.5
elif age > 60:
    fare = fare * 0.7
print("₹", int(fare))

# 9. Time converter
hh, mm = 13, 45
suffix = "AM"
if hh == 0:
    hh = 12
elif hh == 12:
    suffix = "PM"
elif hh > 12:
    hh -= 12
    suffix = "PM"
print(f"{hh}:{mm:02d} {suffix}")

# 10. ASCII classification
ch = '#'
if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Letter")
else:
    print("Special Symbol")

# 11. Grading system
marks = 87
if 90 <= marks <= 100:
    print("A")
elif 85 <= marks <= 89:
    print("B+")
elif 80 <= marks <= 84:
    print("B")
elif 70 <= marks <= 79:
    print("C")
else:
    print("F")

# 12. Currency denomination
amt = 3700
for note in [2000, 500, 100, 50, 20, 10]:
    count = amt // note
    if count:
        print(f"{count}x{note}")
    amt %= note

# 13. Movie ticket
day, age = "Saturday", 10
fare = 200 if day in ["Saturday", "Sunday"] else 150
if age < 12:
    fare *= 0.5
print("₹", int(fare))

# 14. Angle classification
angle = 135
if angle == 90:
    print("Right")
elif angle < 90:
    print("Acute")
elif angle < 180:
    print("Obtuse")
else:
    print("Straight")

# 15. College admission
m1, m2, m3 = 95, 92, 90
avg = (m1+m2+m3)/3
if avg > 90 and min(m1, m2, m3) > 70:
    print("Admitted")
elif avg > 80:
    print("Waitlisted")
else:
    print("Rejected")

# 16. Perfect number
num = 28
div_sum = sum(i for i in range(1, num) if num % i == 0)
print("Perfect" if div_sum == num else "Not Perfect")

# 17. Triangle by angles
a1, a2, a3 = 90, 45, 45
if a1 == 90 or a2 == 90 or a3 == 90:
    print("Right")
elif a1 < 90 and a2 < 90 and a3 < 90:
    print("Acute")
else:
    print("Obtuse")

# 18. GPA scale
marks = 72
if 91 <= marks <= 100:
    print(10)
elif 81 <= marks <= 90:
    print(9)
elif 71 <= marks <= 80:
    print(8)
elif 61 <= marks <= 70:
    print(7)
elif 51 <= marks <= 60:
    print(6)
else:
    print(5)

# 19. Lucky number
num = 1230
s = str(num)
print("Lucky" if int(s[0])+int(s[1]) == int(s[2])+int(s[3]) else "Not Lucky")

# 20. Car insurance
age, exp = 22, 2
if age < 25 and exp < 3:
    print("High Risk")
elif age > 25 and exp > 5:
    print("Low Risk")
else:
    print("Medium Risk")

# 21. Amusement park ticket
age = 65
if age < 12:
    print("₹50")
elif age < 60:
    print("₹100")
else:
    print("₹60")

# 22. Digit classification
num = 45
if num < 10:
    print("Single Digit")
elif num < 100:
    print("Double Digit")
else:
    print("Triple Digit")

# 23. Validate time
hh, mm = 23, 59
if 0 <= hh <= 23 and 0 <= mm <= 59:
    print("Valid")
else:
    print("Invalid")

# 24. Weather categorization
temp = 32
if temp < 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")

# 25. Mobile plan
usage = 6
if usage < 1:
    print("Plan A")
elif usage < 5:
    print("Plan B")
else:
    print("Plan C")

# 26. Duplicate digits
num = 121
s = str(num)
print("Duplicates Present" if len(set(s)) < len(s) else "Unique Digits")

# 27. Weekday classifier
day = 7
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
if day == 7:
    print(f"{days[day-1]} - Weekend")
else:
    print(f"{days[day-1]} - Weekday")

# 28. Attendance eligibility
attended, total = 80, 100
perc = attended/total*100
print("Eligible" if perc >= 75 else "Not Eligible")

# 29. Grade trend
s1, s2, s3 = 60, 70, 80
if s1 < s2 < s3:
    print("Improving")
elif s1 > s2 > s3:
    print("Declining")
else:
    print("Fluctuating")

# 30. Mobile number validation
num = "9876543210"
if len(num) == 10 and num[0] in "6789":
    print("Valid")
else:
    print("Invalid")
