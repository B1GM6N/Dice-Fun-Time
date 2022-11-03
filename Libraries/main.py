import PeytonGermann_Dice
import question
import roll
print("Dice fun time.")
while True:
    answer = question.game_()
    if answer == True:   
        PeytonGermann_Dice.main()
    elif answer == False:
        roll.main()
    elif answer == 3:
        print("BYE")
        break