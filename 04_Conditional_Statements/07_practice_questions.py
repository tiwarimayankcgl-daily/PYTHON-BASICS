# IF STATEMENT PRACTICE
# QUESTION NUMBER= 1

age = int(input("Enter your age :"))
if age >=18: print("Eligible to Vote")

# QUESTION NUMBER = 2

marks = int(input("Enter Your Marks :"))
if marks >= 33: print("Pass")

# QUESTION NUMBER =3

salary = int(input("Enter your salary :"))
if salary >= 50000: print("High salary")

# QUESTION NUMBER = 4

temperature = int(input("Enter temperature :"))
if temperature > 40: print("Heat Wave")

#QUESTION NUMBER = 5

password = input("Enter your password :")
if len(password) >= 8: print("Strong password")

# QUESTION NUMBER = 6

CGPA = float(input("Enter your CGPA :"))
if CGPA >= 8.5: print("Eligible for scholarship")

# If-ELSE PRACTICE QUESTION

age = int(input("Enter your current age :"))
if age >= 18:
    print("You are Adult")
else:
    print("Minor")

# QUESTION NUMBER 8

number = int(input("Enter a number :"))
if number % 2==0:
    print("Number is Even")
else:
    print("Odd number")
    
# QUESTION NUMBER 9

amount = int(input("Enter amount :"))
if amount <= 5000:
    print("Purchase Successful.")
else:
    print("Insufficient Balance")
    
# QUESTUION NUMBER 10

username = input("Enter your username :")
if username == "Mayank":
    print("Welcome ", username)
else:
    print("Invalid username")
    
#QUESTION NUMBER 11
    
marks = int(input("Enter your exam marks"))
if marks >= 35:
    print("PASS")
else:
    print("fAIL")
    
# QUESTION NUMBER 12

internet = True
if internet:
    print("Connected")
else:
    print("No internet")
    
# IF - ELIF -ELSE

# QUESTION NUMBER 13

percentage = int(input("Enter your Obtain Percentage :"))
if percentage >= 90 and percentage <= 100:
    print("Outstanding")
elif percentage >= 75 and percentage < 90:
    print("Excellent")
elif percentage >=60 and percentage < 75:
    print("Good")
elif percentage >=33 and percentage < 60:
    print("Pass")
else:
    print("Fail")
    
    
# QUESTION NUMBER 14


age = int(input("Enter your age :"))
if age > 0 and age <= 12:
    print("Child")
elif age >= 13 and age < 20:
    print("Teenager")
elif age >=20 and age < 60:
    print("Adult")
else:
    print("Senior Citizen")
    
# QUESTION NUMBER 15

BMI = float(input("Enter Your BMI :"))
if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
    
# QUESTION NUMBER 16

month = int(input("Type your month later , (1/2/3) :"))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
else:
    print("Invalid Month")
    
# QUESTION NUMBER 17

bill_units = int(input("Enter your Bill units"))
if bill_units > 0 and bill_units < 100:
    print("Low usage")
elif bill_units >= 100 and bill_units < 200:
    print("Medium Usage")
elif bill_units < 0:
    print("Wrong number")
else:
    print("High Usage")
    

# QUESTION NUMBER 18

experience = int(input("Enter your work experience :"))
if experience >=0 and experience <=1:
    print("Fresher")
elif experience >=2 and experience <=5:
    print("Junior Developer")
elif experience >= 6 and experience <=10:
    print("Senior Developer")
else:
    print("Expert")
    
# QUESTION NUMBER 19

ratings = float(input("Enter movie ratings"))
if ratings >= 9:
    print("Blockbuster")
elif ratings >= 8:
    print("Super Hit")
elif ratings >= 7:
    print("Hit")
else:
    print("Average")

# NESTED IF PRACTICE QUESTION

#QUESTION 20

print("Login system")
username = input("Enter your username :")
password = input("Enter your password :")
if username == "Mayank Tiwari":
    if password == "1234":
        print("Login sucessfully")
    else:
        print("invalid password")
else:
    print("Invalid username")
    
#QUESTION 21

print("ATM MACHINE")
balance = 100000
Correct_PIN= "2004"
withdraw_amount = int(input("Enter your withdraw amount :"))
PIN = input("Enter your pin :")
if balance >= withdraw_amount:
    if PIN == Correct_PIN:
        balance = balance - withdraw_amount
        print("Transaction Successfull.")
        print("Remaining balance :", balance)
    
    else:
        print("Check your pin.")
else:
    print("Insufficient money")
    
    
# 22 number QUESTION

print("Collage Admission")
percentage = int(input("Enter your percentage :"))
Entrance_exam =input("Qualified (Y) , Not Qualified (N) :")
if percentage >= 60:
    if Entrance_exam.upper() == "Y":
        print("Admission confiremed")
    else:
        print("First pass Entrance exam")
else:
    print("Marks doesn't full fill citeria")
    
#23 QUESTION 

print("DRIVING LICENSE")
age = int(input("Enter your age :"))
documents = input("Available (Y) , Not Available (N) :")
if age >= 18:
    if documents.upper() == "Y":
        print("Eligible")
    else:
        print("Documents Required")
else:
    print("Age must be greater than 18")
    
    
# 24 QUESTION 

print("JOB INTERVIEW")
graduation = input("Completed (Y) , Not completed (N) :")
english = input("Good (Y) , Not Good (N) :")
if graduation.upper() == "Y":
    if english.upper() == "Y":
        print("Selected")
    else:
        print("English communication required.")
else:
    print("Graduation is compulsory.")
    
# 25 QUESTION

print("STUDENT MANAGEMENT SYSTEM")
students = ["Aditya", "Mayank", "Rohit", "Surya", "Hero", "Dhoni", "Akash"]
name = input("Enter Your name :").title()
marks = int(input("Enter your marks :"))
attendance = int(input("Enter your total attendance :"))
if name in students:
    if marks >= 33:
        if attendance >= 75:
            print("PASS")
        else:
            print("Fail due to Attendance")
    else:
        print("Fail  due to Marks")
else:
    print("You are not in the students list")
    


            



        

    
