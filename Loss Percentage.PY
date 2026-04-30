CP, SP = map(int, input().split())   # Read Cost Price and Selling Price
loss = CP - SP                       # Calculate loss
loss_percentage = (loss / CP) * 100  # Loss percentage formula
print(f"{loss_percentage:.2f}")      # Print with 2 decimal places
