def ft_merge_list(list1, list2):

    if not list1:
        list1 = []
    if not list2:
        list2 =[]
    
    return sorted(list1 + list2)



# Basic cases
print(ft_merge_list([1, 3, 5, -1], [0, 8, 2, 1]))
# [-1, 0, 1, 1, 2, 3, 5, 8]

print(ft_merge_list([99, -22, 10, 9], []))
# [-22, 9, 10, 99]

# Both lists non-empty
print(ft_merge_list([4, 2], [1, 3]))
# [1, 2, 3, 4]

# One list is None
print(ft_merge_list(None, [5, 3, 1]))
# [1, 3, 5]

print(ft_merge_list([7, 6, 8], None))
# [6, 7, 8]

# Edge cases
print(ft_merge_list([], []))
# []

print(ft_merge_list([1, 1, 1], [1, 1]))
# [1, 1, 1, 1, 1]

print(ft_merge_list([-5, -2], [-3, -1]))
# [-5, -3, -2, -1]