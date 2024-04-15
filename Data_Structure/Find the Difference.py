def findTheDifference(s, t):
    # Initialize a variable to store the XOR result
    result = 0
    
    # XOR all the characters in string s
    for char in s:
        result ^= ord(char)
    
    # XOR all the characters in string t
    for char in t:
        result ^= ord(char)
    
    # The remaining character will be the difference
    return chr(result)

# Test the function
s = "abcd"
t = "abcde"
print(findTheDifference(s, t))