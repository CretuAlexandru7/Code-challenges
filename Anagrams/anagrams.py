

# First try:

# def isAnagram(str1, str2):
#
#     if len(str1) == len(str2):
#         list1 = [i for i in str1]
#         list2 = [i for i in str2]
#
#         for index1, item1 in enumerate(list1):
#             for index2, item2 in enumerate(list2):
#                 if item1 == item2:
#                     list2.pop(index2)
#                     break
#
#         if len(list2) == 0:
#             print("Anagram!")
#             return
#         else:
#             pass
#
#     print("Not Anagram!")

# My second idea is to use dictionaries:  "letter" : no. of apparitions. EX.: 'a' : 3
# At this point in time I know the concept of hash-tables / maps, but I never have implemented one.
# Looking into this tutorial: https://realpython.com/python-hash-table/ I found out about the built-in function ord():
# https://docs.python.org/3/library/functions.html#ord
# ord() is the opposite of chr() and returns the ASCII number of the specific character.
# In this case our problem will become just a sum(of order numbers) == sum(of order numbers).

# def isAnagram(str1, str2):
#     return sum(ord(character1) for character1 in str1) == sum(ord(character2) for character2 in str2)

# And the most obvious one:
# def isAnagram(str1, str2):
#	return sorted(str1) == sorted(str2)

print(isAnagram('anagram', 'nagaram'))
print(isAnagram('anagram', 'nagarrm'))