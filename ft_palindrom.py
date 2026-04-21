def ft_palindrom(string):
    
    rev = ""
    for i in string.lower():
        if i.isalnum():
            rev += i
   
    return  rev == rev[::-1]



# Valid cases
print(ft_palindrom("madam"))                  # True
print(ft_palindrom("racecar"))                   # True
print(ft_palindrom("A man, a plan, a canal: Panama"))  # True
print(ft_palindrom("No 'x' in Nixon"))           # True
print(ft_palindrom(""))                          # True
print(ft_palindrom("a"))                         # True

print(ft_palindrom("hello"))                     # False
print(ft_palindrom("python"))                    # False
print(ft_palindrom("OpenAI"))                    # False

print(ft_palindrom("12321"))                     # True
print(ft_palindrom("12345"))                     # False
print(ft_palindrom("Able was I ere I saw Elba")) # True