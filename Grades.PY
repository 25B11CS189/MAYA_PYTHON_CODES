a,b,c,d,f=map(int,input().split())
maxi=(a+b+c+d+f)//5
if maxi>=90:
    print("Grade A")
elif maxi>=80:
    print("Grade B")
elif maxi>=70:
    print("Grade C")
elif maxi>=60:
    print("Grade D")
elif maxi>=40:
    print("Grade E")
else:
    print("Grade F")
