def ft_pattern(string):
    count = 0
    for i in range(1,len(string)):
        if string[i].isdigit()  and string[i - 1].isdigit():
            if int(string[i]) == int(string[i - 1]) + 1:
                count +=1
            else:
                continue
    return count





# Basic cases
print(ft_pattern("123a345"))  
# 4  -> (1,2), (2,3), (3,4), (4,5)

print(ft_pattern("1a2b3c4d5"))  
# 0  -> no adjacent digits

# Mixed complex case
print(ft_pattern("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
# counts valid pairs like (1,2), (3,4), ..., (8,9)

# Edge cases
print(ft_pattern(""))          
# 0

print(ft_pattern("7"))         
# 0

print(ft_pattern("111111"))    
# 0  -> no increasing sequence

print(ft_pattern("012345"))    
# 5  -> (0,1), (1,2), (2,3), (3,4), (4,5)

print(ft_pattern("98"))        
# 0  -> decreasing, not counted