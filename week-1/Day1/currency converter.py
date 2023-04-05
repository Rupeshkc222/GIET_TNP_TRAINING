def res(a,b):
    if a=="Euro":
        return(b*0.01417)
    if a=="British Pound":
        return(b*0.0100)
    if a=="Australian Dollar":
        return(b*0.02140)
    if a=="Canadian Dollar":
        return(b*0.02027)
    else:
        return(-1)
print(res('Euro',100))
