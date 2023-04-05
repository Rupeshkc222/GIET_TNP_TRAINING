''''Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.
Go through the below program and complete it based on the comments mentioned in it.
Note: Perform case sensitive string comparisons wherever necessary.
'''

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable



def f_l(ticket):
    l=[]
    for i in ticket:
        l.append(i.split(':'))
    d={}
    for i in l:
        if i[0] not in d:
            d[i[0]]=1
        else:
            d[i[0]]+=1
    print("list of airplane with passengers quantiity",d)


ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148",
             "AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
l=f_l(ticket_list)