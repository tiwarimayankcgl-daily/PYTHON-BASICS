age = int(input("Enter your age :"))
if age >= 100:
    print("You are too old for voting.")
elif age >= 18:
    print("You are eligible to give vote.")
elif age < 0:
    print("You not born yet , How do u chat dude.")
else:
    print("You are not aligible to give vote.")
    
#if-elif-else is used when we need more than 2 condition check
# check all block of code , when its find true excuted 
