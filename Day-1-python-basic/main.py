# Day 1 (16/12/2024)

########################### **Variable Address Checking** ###########################
math = 50
chemistry = 50
phy = 50

# Checking memory addresses of variables
print("Address of math:", id(math))
print("Address of chemistry:", id(chemistry))
print("Address of phy:", id(phy))

eng = 40
hin = 40
print("Address of eng:", id(eng))
print("Address of hin:", id(hin))

math = 100
math = 49
print("Address of updated math:", id(math))

############################## **Swapping Two Numbers** ##############################
# Using a temporary variable
num1 = 20
num2 = 40
temp = num1
num1 = num2
num2 = temp

print("After swapping:", num1, num2)

# Swapping without a temporary variable
a = 100
b = 200
a = a + b
b = a - b
a = a - b

print("After swapping without temp variable:", a, b)

########################### **Calculate Percentage of Three Papers** ###########################
p1 = 2
p2 = 10
p3 = 15
percentage = (p1 + p2 + p3) / 3
print("Percentage:", percentage)

############################### **Type Casting Examples** ###############################
# Adding integers
print(2 + 2)

# Concatenating strings
print('2' + '3')

# Type conversion to integer
print(int(3.14))
print(int(True))  # 1
print(int(False))  # 0
print(int("4"))  # Valid conversion from string to int

# Type conversion to float
print(float(True))  # 1.0
print(float(False))  # 0.0
print(float(4))  # 4.0
print(float("4.22"))  # 4.22

# Type conversion to complex
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(5, -3))

############################### **Boolean Operations** ###############################
x = 10
y = 20
print("x is y:", x is y)  # False

############################## **Membership Operator** ##############################
a = "pranjal singh"
print("'pra' in a:", 'pra' in a)  # True

################################# **String Slicing** #################################
name = "pranjalsingh"
print(name[0:5])  # pranj
print(name[1:])  # ranjalsingh
print(name[:])  # pranjalsingh
print(name[1:8:2])  # rjs
print(name[::-1])  # Reverse string

############################### **String Functions** ###############################
s = "python is object oriented programming language"
print(s.find("python"))  # Returns index of "python"
print(s.find("java"))  # -1 (not found)

# Joining strings
s = ["pranjal", "atharv", "ayush"]
m = "$".join(s)
print(m)

# Case conversion functions
s = "python are HIGH LEVEL PROGRAMMING LANGUAGE"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

################################## **If Conditions** ##################################
ch = int(input("Enter any number: "))
if ch > 0:
    print("Positive")
elif ch == 0:
    print("Zero")
else:
    print("Negative")

################################## **For Loop Examples** ##################################
# Print odd numbers
for i in range(1, 10, 2):
    print(i)

# Print multiplication table
for i in range(1, 11):
    print(i * 2, i * 3, i * 4)

# Vowel and consonant counter
name = 'prashantjha'
count_consonant = 0
count_vowel = 0

for i in name:
    if i in "aeiou":
        count_vowel += 1
    else:
        count_consonant += 1

print("Count of vowels:", count_vowel)
print("Count of consonants:", count_consonant)

#################################### **Zip Example** ####################################
for i, j in zip(range(1, 6), range(5, 0, -1)):
    if i == 3 and j == 3:
        continue
    print(i, j)

########################## **Grade Calculation with Gender Check** ##########################
p1 = int(input("Enter paper1 marks: "))
p2 = int(input("Enter paper2 marks: "))
p3 = int(input("Enter paper3 marks: "))
p4 = int(input("Enter paper4 marks: "))
p5 = int(input("Enter paper5 marks: "))

gender = input("Enter your gender (male/female): ")
if p1 >= 40 and p2 >= 40 and p3 >= 40 and p4 >= 40 and p5 >= 40:
    print("You passed!")
else:
    print("You failed!")

total = p1 + p2 + p3 + p4 + p5
percentage = total / 5.0
print("Total Marks:", total)
print("Percentage:", percentage)

if gender == 'male' and percentage >= 60:
    print("Selected")
elif gender == 'female' and percentage >= 65:
    print("Selected")
else:
    print("Not selected")
