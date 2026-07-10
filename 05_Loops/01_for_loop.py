# we used loops to repeat a block of code multiple times. The for loop is one of the most commonly used loops.

for i in range(1, 6):  # range(1, 6) generates numbers from 1 to 5
    print(i)  # This will print numbers from 1 to 5
    
for i in range(1, 11):
    print(i)  # This will print numbers from 1 to 10


for i in range(10, 0, -1):
    print(i) # This will print reverse number from 10 t0 1
    
for i in range(1, 21, 2):
    print(i) # This will print odd number from 1 to 20
    
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
        
number = int(input("Enter a number :"))
for i in range(1, number+1):
    print(i)
    
for i in range(10):
    print("Mayank kumar")