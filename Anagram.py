text1 = input("Enter first word: ")
text2 = input("Enter second word: ")

text1 = text1.upper()
text1 = text1.replace(" ", "")
text2 = text2.upper()
text2 = text2.replace(" ", "")

if text1 == "" or text2 == "":
    print("Empty string cannot be anagram")
else:
    for i in range (len(text1)):
        if text1[i] not in text2:
            print("Not anagrams!")
            break
        else:
            text2 = text2.replace(text1[i], "", 1)
    else:
        if text2 != "":
            print("Not anagrams!")
        else:
            print("Anagrams!")


"""
Sample input: Listen  Silent 
Sample output: Anagrams! 

Sample input: modern   norman 
Sample output: Not anagrams! 
"""
