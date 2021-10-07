# Kacey Mullenhoff
# Feet to Inches
# Converts feet to inches

def main():
    #get input of feet
    feet = float(input("What is the measurement in feet? "))
    # create "inches" variable
    inches = ft_to_inches(feet)
    # print results
    print(f"{feet} feet is equal to {inches:.2f} inches")
    
# define/determine function of feet to inches (multiply by 12)
def ft_to_inches(feet):
    return feet * 12    

main()
