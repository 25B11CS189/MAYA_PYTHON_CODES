A, B = map(int, input().split())   # Read cost per attack and current points
attacks = B // A                   # Integer division gives number of attacks
print(attacks)
