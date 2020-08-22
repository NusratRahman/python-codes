date = input("Enter Birth Date (YYYYMMDD): ")

l = len(date)
while l > 1:
    digitOfLife = 0
    for i in range (l):
        digitOfLife += int(date[i])
    date = str(digitOfLife)
    l = len(date)        

print("Digit of Life: ", digitOfLife)

"""
Sample input: 19991229 
Sample output: 6 

Sample input: 20000101 
Sample output: 4 
"""
