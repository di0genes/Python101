# Kacey Mullenhoff
# Star Pattern (Lab)
# Prints a star pattern with decreasing numbers of stars each iteration (looks like a triangle)
#       *****
#       ****
#       ***
#       **
#       *


BASE_SIZE = int(input("How large would you like the pattern?"))

for r in range(BASE_SIZE):
    for c in range(BASE_SIZE - r):
        print("*", end=' ')
    print()
