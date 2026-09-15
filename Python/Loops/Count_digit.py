# Count digits in  a number
number = int(input("Enter the dgits : "))
Count = 0

while number > 0:
    number = number // 10
    Count = Count + 1

print(f"the digits in the number are : {Count}")

