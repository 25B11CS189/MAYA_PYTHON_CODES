n=int(input())
if n%2==1:
    print("weird")
elif n%2==0 and n<6 and n>1:
    print("not weird")
elif n%2==0 and n>5 and n<21:
    print("weird")
else:
    print("not weird")
