x=int(input())
if x<199:
    c=x*1.2
elif x>=200 and x<400:
    c=x*1.5
elif x>=400 and x<600:
    c=x*1.8
else:
    c=x*2.0
if c>=400:
    sur=c+c*0.15
    print(f"{sur:.2f}")
else:
    sur=c+100
    print(f"{sur:.2f}")
