# Created by Mohammed Mahmud
# Monty Hall Problem
import random
import argparse

# Generates the game!!
def game_generator(time):
    for x in range(0, int(time)):
        value = ["Goat", "Car", "Goat"]
        results = []

        door_one_value = random.choice(value)
        if door_one_value in value:
            value.remove(door_one_value)
        else:
            pass

        door_two_value = random.choice(value)
        if door_two_value in value:
            value.remove(door_two_value)
        else:
            pass

        door_three_value = random.choice(value)
        if door_three_value in value:
            value.remove(door_three_value)
        else:
            pass

        results.append((door_one_value, door_two_value, door_three_value))

        return results


def judgment(user_answer, game_data):
    print(game_data[0][0])
    if int(user_answer) == 0:
        if game_data[0][1] == "Goat":
            print("game_data[1]")
        elif game_data[0][1] == "Goat":
            print("game_data[2]")

    # elif user_answer == 2:
    #     print(1, 3)
    # else:
    #     print(1, 2)


def main():
    print(game_generator(1))
    user = input("witch Door: ")
    judgment(user, game_generator(1))




if __name__ == '__main__':
    main()

# Copyright © by Mohammad Mahmud
