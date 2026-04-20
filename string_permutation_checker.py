def string_permutation_checker(string_1,string_2):
    
    return sorted(string_1) == sorted(string_2)

print(string_permutation_checker("racecar","carrace")) #---> True
print(string_permutation_checker("racecar","carace"))  #---> False
print(string_permutation_checker("Conversation", "Voices rant on")) #--> False