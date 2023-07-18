def power_modules(a,b,c):
    a=a%c
    result=1
    for i in range(b):
        result=(result*a)%c
    return result

a=int(input())
b=int(input())
c=int(input())
print(power_modules(a,b,c))