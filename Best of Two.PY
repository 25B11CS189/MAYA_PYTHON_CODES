a,b,c,x,y,z=map(int,input().split())
if a<b and a<c:
    p=a
elif b<a and b<c:
    p=b
else:
    p=c
if x<y and a<z:
    s=x
elif y<x and y<z:
    s=y
else:
    s=z
if a+b+c-p>x+y+z-s:
    print("Alice")
elif a+b+c-p<x+y+z-s:
    print("Bob")
else:
    print("Tie")
