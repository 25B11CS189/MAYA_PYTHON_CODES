x=int(input())
if x<=10000:
    da=x*0.8
    hr=x*0.2
    y=x+da+hr
    print(f"{y:.2f}")
elif x<=20000:
     da=x*0.9
     hr=x*0.25
     y=x+da+hr
     print(f"{y:.2f}")
else:
     da=x*0.95
     hr=x*0.3
     y=x+da+hr
     print(f"{y:.2f}")
