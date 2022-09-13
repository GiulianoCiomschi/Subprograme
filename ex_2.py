x=int(input("Introdu x: "))
y=int(input("Introdu y: "))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return int(fact)
a=factorial(x)/(factorial(y)*factorial(x-y))
print(a)