#using for loop
sentence = ["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakhs diya or estern lamps","lit up simultaniouslt on the bank of the sarayu river"]
stopword=["for","a","of","the","end","to","in","on","with"]
res=[]
for i in sentence:
    a=i
    for j in i:
        if j in stopword:
            a=a[a.startswith(j)and len(j):]
    res.append([a])
print(res)
#using list comprehension
words = [word for sentence in sentences for word in sentence.split() if word not in stopwords]
print(words)
