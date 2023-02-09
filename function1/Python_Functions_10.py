list = input().split()
def Unique(list):
    u=[]
    for x in list:
        if x not in u:
            u.append(x)
    print(u)
    
Unique(list) 