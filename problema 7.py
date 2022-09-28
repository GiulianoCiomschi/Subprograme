a,b,c,d,e,f,g,h,i,j=int(input("Dati I-ul nr: ")),int(input("Dati II-a nr: ")),int(input("Dati III-a nr: ")),int(input("Dati IV-a nr: ")),int(input("Dati V-a nr: ")),int(input("Dati VI-a nr: ")),int(input("Dati VII-a nr: ")),int(input("Dati VIII-a nr: ")),int(input("Dati IX-a nr: ")),int(input("Dati X-a nr: "))

def max(x,y):
    l=[x,y]
    max=0
    for numar in l:
        if numar>max:
            max = numar
    return max

def min(x,y):
    l=[x,y]
    min=x
    for numar in l:
        if numar<min:
            min = numar
    return min

def min_max(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    S=max(min(x1,x2),max(x3,x4))+min(max(x5,x6),min(x7,x8))
    T=min(x1,x2)+min(x3,x4)+min(x5,x6)+min(x7,x8)+min(x9,x10)
    return print ("S=",S,", iar T=",T)
(min_max(a,b,c,d,e,f,g,h,i,j))