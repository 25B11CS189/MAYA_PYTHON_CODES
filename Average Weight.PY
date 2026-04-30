# Read input values
average, W1, W2 = map(int, input().split())

# Calculate total weight of 3 boys
total = 3 * average

# Find weight of third boy
W3 = total - (W1 + W2)

# Print result
print(W3)
