'''Write a python program that accepts a text and displays a string which contains the word with the largest frequency
 in the text and the frequency itself separated by a space.
Rules:
The word should have the largest frequency. In case multiple words have the same frequency, then choose
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a
single space between the words.
Perform case insensitive string comparisons wherever
necessary.
'''
def check_frequency(l):
    l=l.split(" ")
    # print(l)
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    m_l=[]
    res=""
    m=max(d.values())
    for i in d:
        if d[i] == m:
            m_l.append(i)
            if len(i)>len(res):
                res=i
    print("the answer is ")
    return res,d[res]

a="i am good bad are u good or bad"
print(check_frequency(a))
