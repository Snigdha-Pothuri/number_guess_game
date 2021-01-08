import random
number=random.randint(1,9)
chance=0
while chance<5:
 guess=int(input("Enter a number between 1 and 10 : "))
 if(guess==number):
    print("Congratulations You Won :)")
 elif(guess<number):
    print("Wrong :( Try a bigger number")
 elif(guess>number):
    print("Wrong :( Try a smaller number") 
 chance=chance+1
if not chance<5:
 print("You Lose the number is :",number)
