def readint(prompt, min, max):
    try:
        x = int (input (prompt) )
        assert min<= x <=max
        return x
    except ValueError:
        print("Error: wrong input")
        x = readint("Enter a number from -10 to 10: ", -10, 10)
        return x
    except AssertionError:
        print("Error: the value is not within permitted range (",min,"..",max,")")
        x = readint("Enter a number from -10 to 10: ", -10, 10)
        return x

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)


"""
Sample Input:
Enter a number from -10 to 10: 100
Sample Output:
Error: the value is not within permitted range (-10..10)

Sample Input:
Enter a number from -10 to 10: asd
Sample Output:
Error: wrong input

Sample Input:
Enter number from -10 to 10: 1
Sample Output:
The number is: 1
"""
