text = input("Enter a string: ")

text = text.upper()
text = text.replace(" ", "")

if text == "":
    print("Empty string is not a palindrome")
else:
    textP = text[::-1]
    if text == textP:
        print("It's a Palindrome!")
    else:
        print("It's not a Palindrome!")


"""
Sample input: Ten animals I slam in a net 
Sample output: It's a palindrome 

Sample input: Eleven animals I slam in a net 
Sample output: It's not a palindrome 
"""
