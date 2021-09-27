#   Write a program that calculates the total amount of a meal purchased at a restaurant. The
#   program should ask the user to enter the charge for the food, then calculate the amounts
#   of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total. 

#   Store all values as assigned variables or named constants where appropriate. (This includes tip percentage and tax rate)
#   Use comments at the top of your program to indicate your name, name of program, and short description of what the program in doing. 
#   Comment the meaning of all variables as they are created.
#   All data requests to user should be understandable (user-friendly prompts!)
#   Format output such that numerical values line up (Hint: Use tab special characters!)
#   Remember your output deals with currency. Use the appropriate symbols and correct number of decimal places (use format function!)
#   Declare all variables at the top of your program and give an appropriate default starting value

#Definitions
food_charge = float(input('What is the total of your food? '))
TIP_PERCENT = 18
TAX_PERCENT = 7

#Math
tax = (food_charge * (TAX_PERCENT / 100))
tip = (food_charge * (TIP_PERCENT / 100))

#Final totals and formatting
print(f'Tax ({TAX_PERCENT}%): \t${tax:8,.2f}')
print(f'Tip ({TIP_PERCENT}%): \t${tip:8,.2f}')
print(f'Total: \t\t${tax + tip + food_charge:6,.2f}')

