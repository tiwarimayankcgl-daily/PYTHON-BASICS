# LETS START LOOP 100 QUESTIONS.

# FOR LOOP

for i in range(101, 151):
    print("Roll number :", i) # Student Roll number.
    
    
for i in range(1001, 1021):
    print("Employee id :", i) # Comapny employee id
    
    
numbers = ["9341596137", "8700740710", "9756734211", "9765438756", "8974765634", "9754689765"]
for number in numbers:
    print(number) # Mobile number in the list
    
students = ["Mayank", "Om", "Rohit", "Aditya", "Rahul", "Newton", "Bhola", "Satyam"]
for name in students:
    print(name) # Students name in list
    
cart = ["Laptop", "TV", "Cream", "Perfume", "Keyword", "Heaadphone", "Mouse"]
for item in cart:
    print(item) # shopping cart list
    
number = int(input("Enter your number :"))
for i in range(1, 11):
    print(number, "x", i, "=", number*i) # Table 
    
starting_table = int(input("Enter your start table :"))
End_table = int(input("Enter your end table :"))
for table in range(starting_table, End_table+1):
        print("\nTable of", table)
        for i in range(1, 11):
            print(table, "x", i, "=", table*i) # Table of between 2 numbers
            
marks = [72, 73, 82, 96, 75, 67, 69, 23, 54, 75]
for mark in marks:
    print(mark) # Marksheet
    
marks = [72, 73, 82, 96, 75, 67, 69, 23, 54, 75]

total = 0
for mark in marks:
    total += mark
    print("Total marks =", total) # Total marks
    

marks = [72, 73, 82, 96, 75, 67, 69, 23, 54, 75]
total = 0
count = 0
for mark in marks:
    total += mark
    count += 1
avarage = total/count
print("Total marks =", total)
print("Avarage marks =", avarage)# Avarage 

marks = [72, 73, 82, 96, 75, 67, 69, 23, 54, 75]
highest = marks[0]
for mark in marks:
     if mark > highest:
         highest = mark
print("Highest Marks =", highest) #Highest mark 

marks = [72, 73, 82, 96, 75, 67, 69, 23, 54, 75]
lowest = marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark
print("Lowest mark ", lowest)# lowest mark

name = "Mayank kumar"
count = 0
for letter in name:
    if letter in "aeiouAEIOU":
        count += 1
print("Total Vowels =", count) # Count vowels

name = "Mayank kumar"
for i in name:
    print(i)
    
names = ["mayank", "rohit", "akash"]
for name in names:
    print(name.upper()) #uppercase
    
marks = [75, 28, 90, 31, 66, 45]
for mark in marks:
    if mark > 33:
       print(mark) # 33 se greater marks
       
for i in range(2 , 101, 2):
    print(i) #Even number
    
for i in range(1, 101, 2):
    print(i) # Odd number

prices = [500, 1200, 800, 1500]
for price in prices:
    if price > 1000:
        print("Congrates you got 10% Discount ", price)
        
        
students = ["Mayank", "Rohit", "Akash", "Surya"]
for student in students:
    attendance = input(f"Enter attendance for {students} (present/absent): ")
    print(student, "-", attendance) #Attendance list
    
    
