def shift_alphabet(string,n):
    out_put = ""
    for i in  string:
        if i.isalpha():
            if i >= 'a' and  i <= 'z':
                out_put += chr(((ord(i) - ord('a')) + n) % 26 + ord('a'))
            elif i >= 'A' and  i <= 'Z':
                out_put += chr(((ord(i) - ord('A')) + n) % 26 + ord('A'))
        else:
            out_put += i
    
    return out_put



# Basic cases
print(shift_alphabet("abz", 1))
# "bca"

print(shift_alphabet("AbZ", 1))
# "BcA"

# With spaces and punctuation
print(shift_alphabet("Hello World!", 3))
# "Khoor Zruog!"

# Negative shift
print(shift_alphabet("bca", -1))
# "abz"

# Large shift (wrap around)
print(shift_alphabet("abc", 26))
# "abc"

print(shift_alphabet("xyz", 3))
# "abc"

# Mixed characters
print(shift_alphabet("Python 3.8!", 5))
# "Udymts 3.8!"

# Edge cases
print(shift_alphabet("", 10))
# ""

print(shift_alphabet("12345", 4))
# "12345"