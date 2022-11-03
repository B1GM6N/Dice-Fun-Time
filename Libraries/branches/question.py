# lists
one = ("one","One","1")
two = ("two","Two","2")
three = ("three","Three","3")
play = False
#function
def game_():
    while True:
        print("Would you like to 1 - Play a Game 2 - Roll a dice 3 - leave the program")
        answer = input(">")
        if answer in one:
            play = True
            return play
        elif answer in two:
            play = False
            return play
        elif answer in three:
            play = 3
            return play
        else:
            print("Invalid input.")