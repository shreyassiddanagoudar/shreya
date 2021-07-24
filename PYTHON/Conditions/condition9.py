a=int (input())
b=int (input())
c=int (input())

if(a>b and a>c):
    print("a is oldest among three")
elif( b>c):
    print("b is oldest among three")
else:
    print("c is oldest among three")
if(a<b and a<c):
    print("a is youngest among three")
elif( b<c):
    print("b is  youngest  among three")
else:
    print("c is  youngest  among three")