# Break statement stopes loops whithin conditon become True

for i in range(1, 11):
    
    if i == 6:
        break
    print(i)
    
for i in range(1, 21):
    
    if i == 11:
        break
    print(i)
    
count = 1

while count <= 20:
    if count == 10:
        break
    print(count)
    
while True:
    password = input("Enter your password")
    if password == "Python123":
        print("Login Successful.")
        break
    print("Wrong Password.")
    print("Try Again.")

fruits = ["Apple", "Banana", "Grapes", "litchi", "Orange", "Pomegrand"]
for fruit in fruits:
 if fruit == "Mango":
     break
 print(fruit)