def string_sculptor(string):
    str_1 =""
    found = 0
    k = 0
    for i in string:
        if i.isalpha():
            if k % 2 == 0:
                str_1 += i.lower()
               
            else:
                str_1 += i.upper()
            k +=1
        else:
            str_1 += i

    return str_1


# Basic case
print(string_sculptor("Hello world"))
# "hElLo WoRlD"

# With punctuation
print(string_sculptor("Hello, world!"))
# "hElLo, WoRlD!"

# With numbers
print(string_sculptor("123abcDEF"))
# "123aBcDeF"

# Mixed characters
print(string_sculptor("a-bC-dEf-ghIj"))
# "a-Bc-DeF-gHiJ"

# Edge cases
print(string_sculptor(""))
# ""

print(string_sculptor("12345"))
# "12345"

print(string_sculptor("A"))
# "a"

print(string_sculptor("ab"))
# "aB"