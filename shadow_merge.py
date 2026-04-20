def shadow_merge(list_1 , list_2):
    if list_1 == None:
        list_1 = []
    if list_2 == None:
         list_2 = []
    
    list_t = list_1 + list_2

    return sorted(list_t)



# Basic cases
print(shadow_merge([1, 3, 5, -1], [0, 8, 2, 1]))
# [-1, 0, 1, 1, 2, 3, 5, 8]

print(shadow_merge([99, -22, 10, 9], []))
# [-22, 9, 10, 99]

# Both lists non-empty
print(shadow_merge([4, 2], [1, 3]))
# [1, 2, 3, 4]

# One list is None
print(shadow_merge(None, [5, 3, 1]))
# [1, 3, 5]

print(shadow_merge([7, 6, 8], None))
# [6, 7, 8]

# Edge cases
print(shadow_merge([], []))
# []

print(shadow_merge([1, 1, 1], [1, 1]))
# [1, 1, 1, 1, 1]

print(shadow_merge([-5, -2], [-3, -1]))
# [-5, -3, -2, -1]