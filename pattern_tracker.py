def pattern_tracker(string):
    s_list =[]
    for i in range(len(string )-1):
       if string[i].isdigit() and string[i -1].isdigit() and string[i+1].isdigit():
        if int(string[i]) < int(string[i+1]) + 1:
            s_list.append((i, int(string[i+1]) + 1))
        else:
            continue
    if not s_list:
       return 0
    return s_list

print(pattern_tracker("123a345"))  

print(pattern_tracker("1a2b3c4d5"))
print(pattern_tracker(""))          
print(pattern_tracker("7"))         
print(pattern_tracker("111111"))    
