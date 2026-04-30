CP, SP = map(int, input().split())   # Read Cost Price and Selling Price
profit = SP - CP                     # Calculate profit
percentage = (profit / CP) * 100     # Profit percentage formula
print(f"{percentage:.2f}")           # Print with 2 decimal places
