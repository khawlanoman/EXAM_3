def pattern_tracker(string):
    s_list =[]
    count = 0
    for i in range(len(string)-1):
       if string[i].isdigit() and string[i+1].isdigit():
        if int(string[i]) < int(string[i+1]) + 1:
            count +=1
        else:
            continue
    
    return count


print(pattern_tracker("123a345"))  

print(pattern_tracker("1a2b3c4d5"))
print(pattern_tracker("12asd34hkh45kjhj56jhj67kjhjh78kjhjh89kjhkhj110"))
print(pattern_tracker(""))          
print(pattern_tracker("7"))         
print(pattern_tracker("111111"))    
print(pattern_tracker("98"))        
