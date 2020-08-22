## Seven Segment Display:

one = " #  \n #  \n #  \n #  \n #  "
two = " ###\n   #\n ###\n #  \n ###"
three = " ###\n   #\n ###\n   #\n ###"
four = " # #\n # #\n ###\n   #\n   #"
five = " ###\n #  \n ###\n   #\n ###"
six = " ###\n #  \n ###\n # #\n ###"
seven = " ###\n   #\n   #\n   #\n   #" 
eight = " ###\n # #\n ###\n # #\n ###"
nine = " ###\n # #\n ###\n   #\n ###"
zero = " ###\n # #\n # #\n # #\n ###"

num = []
x = input("Enter a number: ")
for i in range (len(x)):
    y = int(x[i])
    if y == 0: num.append(zero) 
    elif y == 1: num.append(one)
    elif y == 2: num.append(two)
    elif y == 3: num.append(three)
    elif y == 4: num.append(four)
    elif y == 5: num.append(five)
    elif y == 6: num.append(six)
    elif y == 7: num.append(seven)
    elif y == 8: num.append(eight)
    elif y == 9: num.append(nine)

index = 5
for n in num:
    for j in range(4):
        print(n[j], end="")
print()
for n in num:
    for j in range(4):
        print(n[index+j], end="")
print()
index = 10
for n in num:
    for j in range(4):
        print(n[index+j], end="")
print()
index = 15
for n in num:
    for j in range(4):
        print(n[index+j], end="")
print()
index = 20
for n in num:
    for j in range(4):
        print(n[index+j], end="")
