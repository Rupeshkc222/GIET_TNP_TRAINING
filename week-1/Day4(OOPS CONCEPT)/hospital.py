d={"P":"prediatrics","O":"Orthopedics","E":"ENT"}
n=[101,'P',102,'O',302,'O',305,'O']
res={}
for i in range(1,len(n),2):
    print(n[i])
    if n[i] not in res:
        res[n[i]]=1
    else:
        res[n[i]]=res[n[i]]+1
print(res)
ma=0
m_v=""
for i in res:
    if res[i]>ma:
        ma=res[i]
        m_v=i
print(d[m_v])
