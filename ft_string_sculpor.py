def ft_string_sculptor(string):
    k = 1
    out_put = ""
    for i in string:
        if i.isalpha():
            if k % 2 == 0:
                out_put += i.upper()
            else:
                out_put += i.lower()
        else:
            out_put += i
            k = 1
        k +=1
    return out_put


# Basic case
print(ft_string_sculptor("Hello world"))
# "hElLo WoRlD"

# With punctuation
print(ft_string_sculptor("Hello, world!"))
# "hElLo, WoRlD!"

# With numbers
print(ft_string_sculptor("123abcDEF"))
# "123aBcDeF"

# Mixed characters
print(ft_string_sculptor("a-bC-dEf-ghIj"))
# "a-Bc-DeF-gHiJ"

# Edge cases
print(ft_string_sculptor(""))
# ""

print(ft_string_sculptor("12345"))
# "12345"

print(ft_string_sculptor("A"))
# "a"

print(ft_string_sculptor("ab"))
# "aB"