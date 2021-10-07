# Kacey Mullenhoff
# Revised recipe scaling program
# adjusts recipe measurements for desired amount of cookies

# Define main function
def main():
    
# State original ingredient measurements
    cookies_orig=36
    sugar = 1.5
    butter = 0.5
    flour = 2.5
    vanilla =1/48

# Receive input of # cookies and determine general proportion
    num_cookies=float(input('How many cookies would you like? '))/cookies_orig

# Print results
    adjusted_sugar = adjusted_cups(num_cookies, sugar)
    print(f'Sugar = {adjusted_sugar:.2f} cups')
    adjusted_butter = adjusted_cups(num_cookies, butter)
    print(f'Butter = {adjusted_butter:.2f} cups')
    adjusted_flour = adjusted_cups(num_cookies, flour)
    print(f'Flour = {adjusted_flour:.2f} cups')
    adjusted_vanilla = adjusted_cups(num_cookies, vanilla)
    print(f'Vanilla = {adjusted_vanilla * 48:.2f} teaspoons')

# determine proportion of specific ingredient    
def adjusted_cups(num_cookies, ingredient):
    return num_cookies * ingredient

#call main function
main()
