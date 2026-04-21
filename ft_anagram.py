def ft_angram(list1,list2):
    return sorted(list1) == sorted(list2)


print(ft_angram("racecar","carrace")) #---> True
print(ft_angram("racecar","carace"))  #---> False
print(ft_angram("Conversation", "Voices rant on")) #--> Fals