# Range function lets start
print("Range function :")

for i in range(5):
    print(i)
    
# 5 not printed.
# start 0 , end exclude given number

for i in range(1, 6):
    print(i)

# start , stop , step
for i in range(1, 100 , 2):
    print(i)
    
# Reverse counting 
for i in range(10, 0, -1):
    print(i)