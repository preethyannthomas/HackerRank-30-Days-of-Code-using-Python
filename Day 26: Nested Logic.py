# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date
ReturnDate = input().split()
DueDate = input().split()
ReDate = date(int(ReturnDate[2]),int(ReturnDate[1]),int(ReturnDate[0]))
DuDate = date(int(DueDate[2]),int(DueDate[1]),int(DueDate[0]))
if ReDate.year==DuDate.year or ReDate<DuDate:
    if ReDate.month==DuDate.month:
        print((ReDate-DuDate).days*15)
    elif ReDate>DuDate:
        print((ReDate.month-DuDate.month)*500)
    else:
        print('0')
else:
    print("10000")    
