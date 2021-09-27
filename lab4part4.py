a = int(input("Greetings user! Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter the last number: "))

if a > b:
    if a > c:
        print("The largest number is", a)
elif b > c:
        print("The largest number is", b)
else:
    print("The largest number is", c)

    
