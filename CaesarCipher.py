text = input("Enter your message: ")
value = True
while value:
    shift = int(input("Enter shift value 1 .. 25: "))
    if 1<=shift<=25:
        value = False
    else:
        print("You entered wrong value for shift.")

cipher = ''

for char in text:
    if not char.isalpha():
        cipher += char
    elif char.isupper():
        code = ord(char) + shift
        if code > ord('Z'):
            code = 64 + code - ord('Z')
        cipher += chr(code)
    elif char.islower():
        code = ord(char) + shift
        if code > ord('z'):
            code = 96 + code - ord('z')
        cipher += chr(code)

print(cipher)

"""
Sample input: abcxyzABCxyz 123
              2 
Sample output: cdezabCDEzab 123 

Sample input: The die is cast
              25 
Sample output: Sgd chd hr bzrs
"""
