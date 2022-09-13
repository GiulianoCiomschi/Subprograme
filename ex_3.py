x,y=int(input('Introduceti prima fractie: ')),int(input())
q,z=int(input('Introduceti a doua fractie: ')),int(input())
def adunare(a,b,n,m):
    i=(a*m)+(b*n)
    j=b*m
    w=i/j
    return (w)
print(x,'/',y,'+',q,'/',z,'=',adunare(x,y,q,z))

def inmultire(a,b,n,m):
    i=a*n
    j=b*m
    w=i/j
    return (w)
print(x,'/',y,'*',q,'/',z,'=',inmultire(x,y,q,z))