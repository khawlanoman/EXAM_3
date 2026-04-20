def reverse_matrix(s_list):
    t_list =[]
    for k in s_list:
        if isinstance(k, list):
            t_list.append(k[::-1])
    
    return  t_list


# Basic cases
print(reverse_matrix([[1, 2], [3, 4]]))        
# [[2, 1], [4, 3]]

print(reverse_matrix([[1, 2, 3], [4, 5, 6]]))  
# [3, 2, 1], [6, 5, 4]]

# Single row
print(reverse_matrix([[1, 2, 3, 4]]))         
# [[4, 3, 2, 1]]

# Single column
print(reverse_matrix([[1], [2], [3]]))        
# [[1], [2], [3]]

# Edge cases
print(reverse_matrix([[1]]))                 
# [[1]]

print(reverse_matrix([]))                   
# []

# Larger matrix
print(reverse_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

