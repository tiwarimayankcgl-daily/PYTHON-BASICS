#Now work on the nested loop
print("Nested loop :")


for row in range(1, 4):
    for seat in range(1, 5):
        print('Row', row, "Seat", seat)
        
for row in range(1, 4):
    for column in range(1, 4):
        print("Row ", row , "Column", column)
        
for floor in range(1, 4):
    for room in range(1, 5):
        print("Floor", floor, "Room", room)

#This loop is outer loop and inner loop , first inner loop work completed.
#Next outer loop started.
# End this loop we used (break), (Continue), (else):

# For details Knowladge see practice questions .