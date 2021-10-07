# Kacey Mullenhoff
# Book Points Calculator
# Determines the number of points accrued for amount of books purchased

# Obtain number of books purchased
books = int(input("Please enter the number of books purchased: "))
print("You have purchased", books, "books.")
# Check if number of books purchased earns points at all:
if books < 2 :
    print("You have earned 0 points.")

# Check if number of books earns 5 points:   
elif books >=2 and books < 4:
    print("You have earned 5 points.")
    
#Check if number of books earns 15 points:    
elif books >= 4 and books < 6:
    print("You have earned 15 points.")

#Check if number of books earns 30 points:
elif books >=6 and books < 8:
    print("You have earned 30 points.")

#Check if number of books earns 60 points:    
else:
    print("You have earned 60 points.")
