number=6
guess=input("Enter a number between 1 and 10 : ")
if(guess==number):
    print("Congratulations You Won :)")
elif(guess<number):
    print("Wrong :( Try a bigger number")
elif(guess>number):
    print("Wrong :( Try a smaller number")
