def vowels(word):
    count = 0
    for i in word:
        if i in "aeiou":
            count += 1
    return count


def ft_cryptic(s_list):
    return sorted(s_list, key = lambda word : (len(word), word.lower(),vowels(word)))


# Basic cases
print(ft_cryptic(["apple", "bat", "car", "ae", "b"]))
# ['b', 'ae', 'bat', 'car', 'apple']

# Same vowel count, different lengths
print(ft_cryptic(["dog", "cat", "hi", "a"]))
# ['a', 'hi', 'cat', 'dog']

# Same vowel count and length → lexicographical order
print(ft_cryptic(["bat", "cat", "ant"]))
# ['ant', 'bat', 'cat']

# Mixed uppercase and lowercase
print(ft_cryptic(["Apple", "banana", "Kiwi", "grape"]))
# sorted by vowel count (case-insensitive)

# Edge cases
print(ft_cryptic([]))
# []

print(ft_cryptic(["a", "e", "i", "o", "u"]))
# ['a', 'e', 'i', 'o', 'u']

print(ft_cryptic(["bbb", "ccc", "ddd"]))
# ['bbb', 'ccc', 'ddd']  (no vowels, same length → lex order)