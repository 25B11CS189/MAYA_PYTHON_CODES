on,off=map(int,input().split())
on=on-(on*0.1)
if on<off:
    print("ONLINE")
elif off<on:
    print("DINING")
else:
    print("EITHER")
