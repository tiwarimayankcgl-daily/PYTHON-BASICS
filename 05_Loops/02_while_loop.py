# While loop code continuos work untill code of block contain True

count = 1

while count <= 5:
    print(count)
    count += 1
    
count = 1

while count < 11:
    print(count)
    count += 1 # This will print from 1 to 10
    
count = 10

while count >= 1:
    print(count)
    count -= 1
    
number = 0

while number <= 20:
    print(number)
    number += 2
    
number = int(input("Enter a number :"))
count = 1
while count == number:
    print(number)
    count += 1


correct_password = "Python123"
password = input("Enter your password :")
while correct_password != password:
    print("Wrong password.")
    print("Try again")
    password = input("Enter password :")
    print("Login Successfull.")
