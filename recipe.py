# Kacey Mullenhoff
# Recipe scaling program
# adjusts recipe measurements for desired amount of cookies
#    Store all values as assigned variables or named constants where appropriate. (This includes the original recipe values)
#   Comment the meaning of all variables as they are created.
#    All data requests to user should be understandable
#    Declare all variables at the top of your program and give an appropriate default starting value



# Declare variables
#   total
cookies = 36.0
#   Measurements
sugar = 1.5
butter = 0.5
flour = 2.5
#   One cup = 48 teaspoons according to The Internets
vanilla =1/48

#   Prompt for number of cookies desired
cookies_requested=float(input('How many cookies would you like? '))

#   Determine proportions
proportion=cookies_requested / cookies

adjusted_sugar=sugar * proportion
adjusted_butter=butter * proportion
adjusted_flour=flour * proportion
adjusted_vanilla=vanilla * proportion * 48

#   Print new measurements in user-readable format
print("New measurements:")
print(f'Sugar:   {adjusted_sugar:.1f}' " cups")
print(f'Butter: {adjusted_butter:.1f}' " cups")
print(f'Flour:   {adjusted_flour:.1f}'" cups")
print(f'Vanilla: {adjusted_vanilla:.1f}'" tsp")
