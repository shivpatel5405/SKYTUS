number = int(input("Enter the numbers : "))
reverse = 0
while number>0:
    digit = number%10                     # gets the last digit
    reverse = reverse * 10 + digit        # adds that digit to the reversed number
    number = number//10                   # removes the last digit
    
print(f"The number in reversed form is {reverse}")