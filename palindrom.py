def is_palindrome(string):
    is_string=""
    for i in string.lower():

        if i.isalnum():
            is_string += i
    
    
    if is_string == is_string[::-1]:
        return True
    
    return  False


# Valid cases
print(is_palindrome("madam"))                    # True
print(is_palindrome("racecar"))                # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("No 'x' in Nixon"))           # True
print(is_palindrome(""))                          # True
print(is_palindrome("a"))                         # True

# Invalid cases
print(is_palindrome("hello"))                     # False
print(is_palindrome("python"))                  # False
print(is_palindrome("OpenAI"))                    # False

# Edge cases
print(is_palindrome("12321") )                    # True
print(is_palindrome("12345"))                     # False
print(is_palindrome("Able was I ere I saw Elba")) # True