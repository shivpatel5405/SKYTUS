# Find the Sum of Even numbers between 1-100
Total = 0
for i in range(1,101):
    if i % 2 == 0:
        Total = Total + i
print(f"The sum of even number between 1-100 : {Total}")