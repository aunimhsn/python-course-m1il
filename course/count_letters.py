text = "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth. \
"

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = {}

for char in alphabet:
    result[char] = text.count(char)

print(result)


# Solution 1
# result = {}
# text = text.lower()
# for char in text:
#     if char in result.keys():
#         result[char] += 1
#     else:
#         result[char] = 1

# print(result)


# Solution 2 - count()
# result = {}
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     result[char] = text.lower().count(char)

# print(result)


# Solution 3 - collections.Counter()
# from collections import Counter
# result = Counter(text.lower())

# print(result)