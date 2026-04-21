def ft_twister(s_list, number):
    
    if len(s_list) == 0:
        return s_list
    number  = number % len(s_list)
    return s_list[-number::] + s_list[:-number]


# Basic cases
print(ft_twister([1, 2, 3, 4, 5], 2))
# [4, 5, 1, 2, 3]

print(ft_twister([4, 2, 1, -1, 'a'], 4))
# [2, 1, -1, 'a', 4]

# Rotation equal to length
print(ft_twister([1, 2, 3], 3))
# [1, 2, 3]

# Rotation greater than length
print(ft_twister([1, 2, 3], 5))
# [2, 3, 1]

# Negative rotation (left rotation)
print(ft_twister([1, 2, 3, 4], -1))
# [2, 3, 4, 1]

# Edge cases
print(ft_twister([] , 3))
# []

print(ft_twister([1], 10))
# [1]