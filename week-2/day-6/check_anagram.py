'''Write a python function, check_anagram() which accepts two
strings and returns True, if one string is an anagram of
another string.
Otherwise returns False.
The two strings are considered to be an anagram if they
 contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same.
'''
def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    s1_list = sorted(list(s1))
    s2_list = sorted(list(s2))
    if s1_list == s2_list:
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                return False
        return True
    else:
        return False
a=check_anagram("rupesh","urephs")
print(a)