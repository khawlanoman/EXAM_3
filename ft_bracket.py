def ft_bracket(string):
    stack = []
    dict ={
        "}":"{",
        ")":"(",
        "]":"["
    }
    for i in string:
        if i in dict.values():
            stack.append(i)
        elif i in dict:
            if not stack or stack[-1] != dict[i]:
                return False
            stack.pop()
    if stack:
        return False
    
    return True


print(ft_bracket("()"))           # True
print(ft_bracket("()[]{}"))       # True
print(ft_bracket("{[()]}"))       # True
print(ft_bracket("")    )         # True  (empty string is valid)
print(ft_bracket("hello(hhhh)world{ho}w are"))  #True

# Invalid cases
print(ft_bracket("(]"))           # False
print(ft_bracket("([)]"))         # False
print(ft_bracket("(((") )         # False
print(ft_bracket("())"))          # False
print(ft_bracket("{[(])}"))       # False
    
