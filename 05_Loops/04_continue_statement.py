# Skip the cureent iteration and go to the next iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
fruites = ["Apple", "Banana", "Orange", "Grapes", "litchi"]
for fruit in fruites:
    if fruit == "Apple":
        continue
    print(fruit)
    
for i in range(0, 21, 2):
    if i == 12:
        continue
    print(i)
    