#Szymon Jaworski, 367072, Grupa 1
#Zadanie 4

def fun(lst,n):
    tmp = lst.copy()

    for i in range(len(tmp)):
        tmp[i] = lst[(i-n)%len(tmp)]
        
    return tmp

