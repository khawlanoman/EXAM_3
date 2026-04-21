def ft_reverse_m(s_list):
    t_list = []
    for i in s_list:
        t_list.append(i[::-1])
    
    return (t_list)



print(ft_reverse_m([[1, 2], [3, 4]]))        
# [[2, 1], [4, 3]]

print(ft_reverse_m([[1, 2, 3], [4, 5, 6]]))  
# [3, 2, 1], [6, 5, 4]]

# Single row
print(ft_reverse_m([[1, 2, 3, 4]]))          
# [[4, 3, 2, 1]]

# Single column
print(ft_reverse_m([[1], [2], [3]]))         
# [[1], [2], [3]]

# Edge cases
print(ft_reverse_m([[1]]))                   
# [[1]]

print(ft_reverse_m([]))                      
# []

# Larger matrix
print(ft_reverse_m([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]