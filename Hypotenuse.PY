import math

X, Y = map(int, input().split())   # Read two sides
hypotenuse = math.sqrt(X*X + Y*Y)  # Apply Pythagoras theorem
print(f"{hypotenuse:.2f}")         # Print with 2 decimal places
