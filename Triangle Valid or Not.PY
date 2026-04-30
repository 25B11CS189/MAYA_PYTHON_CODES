x,y,z=map(int,input().split())
if (x+y)>z and (y+z)>x and (z+x)>y:
    print("Valid triangle")
else:
    print("Invalid triangle")
