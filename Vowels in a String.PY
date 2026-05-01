s = input().strip()
v = input().strip()

if v in s:
    print("True")
    print(s.index(v))
else:
    print("False")
