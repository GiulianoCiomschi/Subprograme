list1=[]
def creare_list():
    n=int(input('Dați nr de elemente: '))
    list=[]
    for i in range(n):
        y=eval(input('Elementul '+str(i)+' este: '))
        while type(y)!=int:
            y=eval(input('Introduceti doar elemente de tip int! Elementul '+str( i)+' este: '))
            if type(yt)==int:
                break
        list.append(y)
    return list
list1=creare_list()
print(list1)