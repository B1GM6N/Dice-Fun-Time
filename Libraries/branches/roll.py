import random
def person_roll_dice(dc):
    total = 0
    x = 1
    while x <= int(dc):
        roll = random.randint(1,6)
        print(f"You rolled a {roll}.")
        total = total + roll
        x = x + 1
    return total
def main():
    while True:
        print("How many dice would you like to roll?")
        number = input(">")
        try:
            int(number)
            break
        except:
            ValueError
    person_roll_dice(number)