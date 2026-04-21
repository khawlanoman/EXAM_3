def ft_shift_alpha(string, num):
    out_put = ""
    for i in string:
        if i.isalpha():
            if i >= 'a' and i <= 'z':
                out_put += chr(((ord(i) - ord('a')) + num)% 26 + ord('a'))
            elif i >= 'A' and i <= 'Z':
                out_put += chr(((ord(i) - ord('A')) + num)% 26 + ord('A'))
        else:
            out_put += i

    return out_put


# Basic cases
print(ft_shift_alpha("abz", 1))
# "bca"

print(ft_shift_alpha("AbZ", 1))
# "BcA"

# With spaces and punctuation
print(ft_shift_alpha("Hello World!", 3))
# "Khoor Zruog!"

# Negative shift
print(ft_shift_alpha("bca", -1))
# "abz"

# Large shift (wrap around)
print(ft_shift_alpha("abc", 26))
# "abc"

print(ft_shift_alpha("xyz", 3))
# "abc"

# Mixed characters
print(ft_shift_alpha("Python 3.8!", 5))
# "Udymts 3.8!"

# Edge cases
print(ft_shift_alpha("", 10))
# ""

print(ft_shift_alpha("12345", 4))
# "12345"