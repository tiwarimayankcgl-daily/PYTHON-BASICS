# ARITHMETIC OPERATORS
# 1

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
 
print(f"Addition of two number is : {a+b} ")
print(f"Substraction of two number is : {a-b}")
print(f"Multiplication of two number is : {a*b}")
print(f"Divison of two number is : {a/b}")
print(f"Flour division of two number is : {a//b}")
print(f"Modules of two number is : {a%b}")
print(f"Exponent of two number is : {a**b}")

#2

lenghth= float(input("Enter lenghth of rectangle :"))
width = float(input("Enter width of rectangle :"))
print(f"Area of a rectangle is : {lenghth * width}")
print(f"Perimeter of a rectangle is : {2.0*(lenghth + width)}")

#3

sub1 = int(input("Enter first subjects marks :"))
sub2 = int(input("Enter second subjects marks :"))
sub3 = int(input("Enter third subjects marks :"))
sub4 = int(input("Enter fourth subjects marks :"))
sub5 = int(input("Enter fifth subjects marks :"))
total = sub1+sub2+sub3+sub4+sub5
avarage = total / 5
print(f"Total marks of student is : {total}")
print(f"Avarage mark of student is : {avarage}")


#ASSIGNMENT OPERATOR

salary = int(input("Enter current salary"))
print("Current salary is :", salary)
salary += 5000
print(f"Encresed salary is : {salary}")

#2

balance = 10000
balance += 3000
print("YOUR BALANCE IS :", balance)
balance -= 1500
print("Your decresed balance is :",  balance)
balance /= 2
print("Your divided balance is :", balance) 

#3

marks = 50
marks += 20
marks *= 2
marks -= 40
print("Your marks is :", marks)

# COMPARISON OPERATORS

#1

age = int(input("Enter your current age :"))
print(f"YOU ARE GREATER THAN 18 :", {age > 18})
print(f"YOU ARE LOWER THAN 18 :", {age < 18})
print(f"YOU ARE EQUEL THAN 22 :", {age == 22})
print(f"YOU ARE GREATER THAN AUR EQUAL TO 25 :", {age != 25})
print(f"YOU ARE GREATER THAN 18 :", {age >= 18})
print(f"YOU ARE GREATER THAN 18 :", {age <= 18})

# Make this code output clean and senseble its your task

#2

a = 100
b = 50

print("a greater than b :", {a > b})
print("a lower than b :", {a < b})
print("a greater than or equeal to  b :", {a >= b})
print("a lower than  or equeal to b :", {a <= b})
print("a not equal to b :", {a != b})
print("a equeal to  b :", {a == b})

#3

marks = 78
print(f"PASS :", {marks > 60})
print(f" MORE THAN 90 :", {marks > 90})
print(f"MARKS IS EQUEAL TO 100 :", {marks == 100})

# LOGICAL OPERATORS

#1

age = 20
has_id = True
print("Approved :", age >=18 and has_id)
print("Not Approved :", age < 18 and has_id)
print(not(has_id))

#2

attendence = 80
fees_paid = True
print("You are eligible for exam :", attendence >= 75 and fees_paid)


#3

username = True
password = False
print("YOU CAN LOGIN :", username and password)
print("YOU ARE LOGGINED :", username and not(password))

# IDENTITY OPERATORS

a = 50
b = 50
c = 100

print(a is b)
print(a is c)
print(b is not c)

#2

x = "python"
y = "python"
z = "java"
print(x is y)
print(x is z)
print(y is not z) 

#MEMBERSHIP OPERATOR

programming = ["Python", "java", "Sql", "Excel", "Power BI"]
print("YES :", "Sql" in programming)
print("YES :", "java" in programming)
print("NO :", "R" not in programming)
print("NO :", "C++" not in programming)

#2

name = "Mayank Kumar"
print("M" in name)
print("K" in name)
print("Z" not in name)

#3

fruites = ("Apple", "Banana", "Mango")
print("Apple" in fruites)
print("Orange" not in fruites)

#BITWISE OPERATOR
#1

a = 12
b = 10
print(a & b)
print(a != b)
print(a ^ b)
print(~b)

#2

number = 8
print(number << 1)
print(number >> 1)

# BONUS PROGRAMM INCLUDE ALL OPEARATORS

print("========== BONUS PROGRAM ==========\n")

# Arithmetic Operators
a = 20
b = 6

print("Arithmetic Operators")
print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponent :", a ** b)

print("\n==============================\n")

# Assignment Operators
x = 10

x += 5
print("After += :", x)

x -= 2
print("After -= :", x)

x *= 3
print("After *= :", x)

x /= 2
print("After /= :", x)

print("\n==============================\n")

# Comparison Operators
p = 15
q = 10

print("Comparison Operators")
print("p == q :", p == q)
print("p != q :", p != q)
print("p > q :", p > q)
print("p < q :", p < q)
print("p >= q :", p >= q)
print("p <= q :", p <= q)

print("\n==============================\n")

# Logical Operators
age = 20
has_id = True

print("Logical Operators")
print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

print("\n==============================\n")

# Identity Operators
m = 50
n = 50

print("Identity Operators")
print(m is n)
print(m is not n)

print("\n==============================\n")

# Membership Operators
languages = ["Python", "SQL", "Excel", "Power BI"]

print("Membership Operators")
print("Python" in languages)
print("Java" in languages)
print("Excel" not in languages)
print("C++" not in languages)

print("\n==============================\n")

# Bitwise Operators
num1 = 12
num2 = 10

print("Bitwise Operators")
print("AND :", num1 & num2)
print("OR :", num1 | num2)
print("XOR :", num1 ^ num2)
print("NOT :", ~num1)
print("Left Shift :", num1 << 1)
print("Right Shift :", num1 >> 1)

print("\n========== END ==========")