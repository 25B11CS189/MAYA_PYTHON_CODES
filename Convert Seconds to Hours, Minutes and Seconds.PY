seconds = int(input())          # Read total seconds
hours = seconds // 3600         # 1 hour = 3600 seconds
seconds %= 3600
minutes = seconds // 60         # 1 minute = 60 seconds
seconds %= 60
print(f"H:M:S-{hours}:{minutes}:{seconds}")
