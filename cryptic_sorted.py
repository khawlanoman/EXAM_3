def vowels(word):
    count = 0
    for i in word.lower():
        if i in "aeiou":
            count +=1
    
    return count

def cryptic_sorter(s_list):

    return sorted(s_list, key= lambda word : (len(word),word.lower(), word.upper(), vowels(word)))



# Basic cases
print(cryptic_sorter(["apple", "bat", "car", "ae", "b"]))
# ['b', 'ae', 'bat', 'car', 'apple']

# Same vowel count, different lengths
print(cryptic_sorter(["dog", "cat", "hi", "a"]))
# ['a', 'hi', 'cat', 'dog']

# Same vowel count and length → lexicographical order
print(cryptic_sorter(["bat", "cat", "ant"]))
# ['ant', 'bat', 'cat']

# Mixed uppercase and lowercase
print(cryptic_sorter(["Apple", "banana", "Kiwi", "grape"]))
# sorted by vowel count (case-insensitive)

# Edge cases
print(cryptic_sorter(["APPLE","apple","Apple"]))
# []

print(cryptic_sorter(["a", "e", "i", "o", "u"]))
# ['a', 'e', 'i', 'o', 'u']

print(cryptic_sorter(["bbb", "AAA", "BBB", "aaa"]))
# ['bbb', 'ccc', 'ddd']  (no vowels, same length → lex order)