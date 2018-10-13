# Created by Mohammed Mahmud
# Monty Hall Problem
import random


# Generates the game!!
def game_generator(how_many_time_gen_game):
    results = []
    # Will run the loop based on how_many_time_gen_game
    for x in range(0, int(how_many_time_gen_game)):
        value = ["Goat", "Car", "Goat"]

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


def judgment(game_data):
    WinnerOrloser = ""
    SchoolKeeper = []
    gmae_num = 0
    for x in game_data:
        user_pick_dore = random.randint(1, 3)
        if user_pick_dore == 1:

            if game_data[0][0] == "Goat":
                WinnerOrloser = "loser"
            else:
                WinnerOrloser = "Winner"

        elif user_pick_dore == 2:
            if game_data[0][1] == "Goat":
                WinnerOrloser = "loser"
            else:
                WinnerOrloser = "Winner"

        elif user_pick_dore == 3:
            if game_data[0][2] == "Goat":
                WinnerOrloser = "loser"
            else:
                WinnerOrloser = "Winner"

        # {"UserPickNum": user_pick_dore, "WinnerORLoser": WinnerOrloser, "Result": x}
        # {'firstname': ["Mr.", " ghj"], 'lastname': "My Father's Son"}
        gmae_num += 1
        # SchoolKeeper.append([num, x, user_pick_dore, WinnerOrloser])
        SchoolKeeper.append({'firstname': [gmae_num, x], 'lastname': [user_pick_dore, WinnerOrloser]})

    return SchoolKeeper


def main(how_many_game, switch_or_not):
    game_gen = game_generator(int(how_many_game))
    return judgment(game_gen)
