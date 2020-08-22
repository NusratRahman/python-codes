import sys

l = []
for i in range (9):
    print("Enter row", i+1, ": ", end = "")
    l.append(input())

# checking ROW:
for j in range (9):
    for k in range (9):
        if str(k+1) not in l[j]:
            print("Not a Sudoku.")
            sys.exit()

# checking COLUMN:
for i in range (9):
    digit = "123456789"
    for j in range (9):
        check = l[j][i:i+1]
        if check not in digit:
            print("Not a Sudoku.")
            sys.exit()
        else:
            digit = digit.replace(check, "")

# checking Sub-Squares:
def subSquare (r, k):
    digit = "123456789"
    c = k
    for i in range (3):
        for j in range (3):
            check = l[r][c:c+1]
            if check not in digit:
                print("Not a Sudoku.")
                sys.exit()
            else:
                digit = digit.replace(check, "")
                c += 1
        r += 1
        c = k

subSquare (0, 0)
subSquare (0, 3)
subSquare (0, 6)
subSquare (3, 0)
subSquare (3, 3)
subSquare (3, 6)
subSquare (6, 0)
subSquare (6, 3)
subSquare (6, 6)

print ("Yes, It's a SUDOKU")

"""
Sample input:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672 
Sample output: Yes, It's a SUDOKU 

Sample input:
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671 
Sample output: Not a Sudoku

"""

