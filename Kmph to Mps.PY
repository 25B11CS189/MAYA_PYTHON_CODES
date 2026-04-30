speed_kmph = int(input())              # Read speed in km/h
speed_mps = speed_kmph * 1000 / 3600   # Convert to m/s
print(f"{speed_mps:.2f}")              # Print with 2 decimal places
