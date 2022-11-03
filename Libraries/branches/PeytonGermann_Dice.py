##############################
# Summative #2 - Dice Roller
# Peyton Germann
# Friday, October 8, 2021
##############################

# Functions #
#rolls persons dice and adds it to the total
import random
def nam():
    print("What is your name?")
    nm = input(">")
    return nm

def person_roll_dice(nm,dc):
    total = 0
    x = 1
    while x <= int(dc):
        roll = random.randint(1,6)
        print(f"{nm}'s {x} dice rolled a {roll}.")
        total = total + roll
        x = x + 1
    return total
#rolls computer dice and adds it to the total
def computer_roll_dice(dc):
    total = 0
    x = 1
    while x <= int(dc):
        roll = random.randint(1,6)
        print(f"Bob's {x} dice rolled a {roll}.")
        total = total + roll
        x = x + 1
    return total
# Slows the program so the person can read what it says
def slow_time(time):
    from time import sleep
    sleep(time)
    
# Main Code #
def main():
    name = nam()
    print("\nWelcome to a dice rolling battle between human and computer! My name is Bob The Computer. Good Luck.")
    #Determines how many times the dice will roll
    dice_number = input("\nHow many dice would you like to roll?\n")
    #returns total as your_total
    your_total = person_roll_dice(name,dice_number)
    #prints total for the user
    print(f"\nYour total is {your_total}.")
    #funny competetive message
    slow_time(2)
    print("\nYou are doing alright for a human.\n")
    
    slow_time(3)
    
    print("\nNow it is Bob's turn!")
    #returns total as bob_total
    bob_total = computer_roll_dice(dice_number)
    #prints computer total
    print(f"\nBob's total is {bob_total}.")
    
    slow_time(4)
    #Win, Loss, and Tie messages
    if bob_total > your_total:
        print("\nLOL. Looks like Bob beat you with my epic luck!")
    
    if bob_total < your_total:
        print("\nLooks like you won. Good game!")
    
    if bob_total == your_total:
        print("\nLooks like Bob and Human tied. We should have a rematch!")
    slow_time(2)