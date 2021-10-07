# Kacey Mullenhoff
# Average to Letter Grade Converter
# Determines the letter grade of the average of five test scores.

def main():
    # Get scores from user
    first_score = float(input("Please enter your first score: "))
    second_score = float(input("Please enter your second score: "))
    third_score = float(input("Please enter your third score: "))
    fourth_score = float(input("Please enter your fourth score: "))
    final_score = float(input("Please enter your final score: "))

    # pass average to variable in main
    avg = calc_average(first_score, second_score, third_score, fourth_score, final_score)

    # print final average and letter grade  
    print (determine_grade(avg))
    
#calculate average    
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

# determine letter grade
def determine_grade(avg):
    if avg < 60:
        return f"Your grade is: {avg} = F"
    elif avg <70 and avg >= 60:
        return f"Your grade is: {avg} = D"
    elif avg <80 and avg >= 70:
        return f"Your grade is: {avg} = C"
    elif avg <90 and avg >= 80:
        return f"Your grade is: {avg} = B"
    else:
        return f"Your grade is: {avg} = A"

main()
