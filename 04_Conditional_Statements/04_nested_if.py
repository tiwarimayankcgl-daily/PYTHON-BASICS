age =int(input("Enter your age :"))
has_license = True
if age >= 18:
    if has_license:
        print("You can give vote.")
    else:
        print("You need a license.")
else:
    print("You can not give vote.")
    
# Nested if is the one if under the another if
