#This is a pretty standard Leetcode problem where you are given a 'roman' numeral and told to convert it into an interger output. The end should be a function where you can call it, it inputs a string roman numeral and outputs an integer.

#In order to acomplish this you need to understand the ditionary of Roman numerals. 'I' = 1, 'V' = 5,'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1,000

#further, you have to understand the logic behind the Roman numerial system. The 'I' or 1 is a float that floats in either the -1 or +1 position to indicate a 4,5, or 9. Example 19 = XIX or 10, -1, 10.

#you have to build out a function that captures all of this logic and the creates a numeral. You can do a brute force dictionary method but this is not effective. It is far better to simply create a logic function that checks to see how the 'I' is floated arond the number.

#here is the basics of how to code operates.

def romanToInt(s: str) -> int:
    # Dictionary with values for Roman numerals
    ROMANS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Variable for accumulating total
    number = 0

    # Process all characters except the last one
    for i in range(len(s) - 1):
        if ROMANS[s[i + 1]] > ROMANS[s[i]]:
            number -= ROMANS[s[i]]
        else:
            number += ROMANS[s[i]]

    # Process last character
    number += ROMANS[s[len(s) - 1]]

    return number

roman_num= input('Give me a roman number and I will convert it\n')
conv_n = romanToInt(s=roman_num)
print(f"When converted your roman number is {conv_n}")