name = input("Type your name: ")
print("Welcome "+ name+ " to this adventure")

answer = input("You are on a dirt road it has come to an end and you can go left and right. which way you want to go (right/left)? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim acccross: (swim/walk)  ")

    if answer == 'swim':
        print("You swim across and eaten by alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge, it look wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == 'back':
        print("You go back and loose")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger, Do you talk to them (Yes/No)? ")
        if answer == 'yes':
            print("Good Job! You got a gold coin from stanger and won this adventure.")

        elif answer == 'no':
            print("You ignore the stranger. They are offended and they kill you. You loose.")

        else:
            print("Not a valid option. You loose.")
        
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose")


print("Thank you for trying", name)