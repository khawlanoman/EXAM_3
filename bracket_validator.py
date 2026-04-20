def bracket_validator(string):

    dict  = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    stack = []
    for i in string:
        if i in dict.values():
            stack.append(i)
        
        elif i in dict:
            if not stack or stack[-1] != dict[i]:
                return False
            stack.pop()
        elif i.isalpha():
            continue
    if stack:
        return False
    
    return True


print(bracket_validator("()") )          # True
print(bracket_validator("()[]{}"))       # True
print(bracket_validator("{[()]}"))     # True
print(bracket_validator(""))          # True  (empty string is valid)
print(bracket_validator("hello(hhhh)world{ho}w are"))  #True

# Invalid cases
print(bracket_validator("(]"))      # False
print(bracket_validator("([)]"))         # False
print(bracket_validator("((("))     # False
print(bracket_validator("())") )     # False
print(bracket_validator("{[(])}") )      # False