print("Welcome to my computer quiz!")

playing = input('Do you want to play? ')

if playing.lower() != "yes":
    print("Thank you for the time! :)")
    quit()
    

print("Let's Play :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Yayy! Correct")
    score += 1
else:
    print(":( Wrong")


answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
     print("Yayy! Correct")
     score += 1
else:
    print(":( Wrong")

answer = input("What does RAM stand for? ")

if answer.lower() == "random acess memory":
     print("Yayy! Correct")
     score += 1
else:
    print(":( Wrong")

answer = input("What does ROM stand for? ")

if answer.lower() == "read only memory":
     print("Yayy! Correct")
     score += 1
else:
    print(":( Wrong")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
     print("Yayy! Correct")
     score += 1
else:
    print(":( Wrong")


print(f"You got {(score)} out of 5 questions.")
print(f"You got {(score/4)  * 100}% in this quiz")