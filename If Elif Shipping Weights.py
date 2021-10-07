# Kacey Mullenhoff
# Shipping Charges
# Determines rate tier and final price of shipping charges for various weights


#Determine number of pounds to ship:
lbs=float(input("Please input package weight: "))

#Check if less than or equal to 2lbs:
if lbs <= 2:
    print("Rate per pound: $1.50")
    print(f'Total shipping charges: ${lbs * 1.50:.2f}')

#Check if between 2 and 6 lbs:
elif lbs > 2 and lbs <= 6:
    print("Rate per pound: $3.00")
    print(f'Total shipping charges: ${lbs * 3:.2f}')

#Check if between 6 and 10 lbs:
elif lbs > 6 and lbs <= 10:
    print("Rate per pound: $4.00")
    print(f'Total shipping charges: ${lbs * 4:.2f}')

# If over 10 lbs:
else:
    print("Rate per pound: $4.75")
    print(f'Total shipping charges: ${lbs * 4.75:.2f}')
