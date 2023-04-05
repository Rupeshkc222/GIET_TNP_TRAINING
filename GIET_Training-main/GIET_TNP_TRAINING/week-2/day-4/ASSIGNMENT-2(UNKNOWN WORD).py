'''Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words.
The task is to find the unknown words (other than the words they already know) from the given text.
Write a python function which accepts the text and the known list of words and returns the set of unknown words found.

Return -1 if there are no unknown words.

Sample Input

Text: "the sun rises in the east"

Vocabulary: ["sun", "in", "east", "doctor", "day"]

Expected Output

{'rises', 'the'}'''

def l_find(s,v):
    l=[]
    for i in s:
        if i not in v and i not in l:
            l.append(i)
    return l

s="the sun rises in the east"
s=s.split(" ")
print(s)
V=["sun", "in", "east", "doctor", "day"]
print(l_find(s,V))