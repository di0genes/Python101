# Kacey Mullenhoff
# Budget Flowchart (Lab)
# Checks expenses against a monthly budget
# Get the first item of the budget or press 0 to end
# Get budget value
print("Greetings! What is your budget this month? Press 0 when finished:")
budget = float(input("Budget: "))
# Set initial values
total=0

## Unsure if this is an appropriate use here but it works- would () be considered a null value or placeholder of some sort? 
item=()

# While budget is not 0, continue requesting items
while item != 0:

    #get the value of the first item to be added to the budget
    item = float(input("Enter the value of the item you have spent or press 0 to end: "))
    #Increment the amount as items are added
    total += item
    #Print total value of items
    print(f"${total:.2f}")

#Determine whether total value of items is over, under, or hits budget
    print("Enter the value of the next item you have spent or press 0 to end")
if total == budget:
    print(f"${total:.2f} - You have hit your budget limit.")
elif total < budget:
    print(f"${total:.2f} - You are still within your budget.")
else:
    print(f"${total:.2f} - You are over your budget.")
