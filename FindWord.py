text1 = input("Enter a word: ")
text1 = text1.upper()

text2 = input("Enter a string to search into: ")
text2 = text2.upper()
text2 = text2.replace(" ", "")

for i in range (len(text1)):
    pos = text2.find(text1[i])
    if pos == -1:
        print("No")
        break
    else:
        text2 = text2[pos+1:]
else:
    print("Yes")

"""
Sample input: donor Nabucodonosor  
Sample output: Yes 

Sample input: donut Nabucodonosor  
Sample output: No 
"""
