import random
import re
import sys

def get_input(prompt):
    user_input = input(prompt)
    exit_commands = ["q", "quit", "exit"]

    if user_input.lower() in exit_commands:
        print("Exiting program...")
        sys.exit()
    return user_input

def roll(num_dice, dice_size):
    i = 0
    result = 0
    while i < num_dice:
        result += random.randint(1, dice_size)
        i += 1
    return result

def target_selection(creatures):
    i = 1
    print("possible targets:")
    for creature in creatures:
        if creature["type"] == "NPC":
            print(f"{i}: {creature["name"]}, hp:{creature["current_hp"]} / {creature["max_hp"]}, conditions: {creature["conditions"]}")
        else:
            print(f"{i}: {creature["name"]}, conditions: {creature["conditions"]}")
        i += 1
    #save the index of the target
    while True:
        target = get_input("Write the number in front the target:")
        pattern = re.compile(r"^(\d+)$")
        match = pattern.search(target)
        if match and 0 < int(target) < len(creatures)+1:
            target_index = int(target) - 1
            break
        else:
            print(f"Incorrect entry, please enter the number before the target, it is supposed to be between 1 and {len(creatures)+1}")
    return creatures[target_index]

def input_roll():
    while True:
        print("Write the number directly or if you want to roll write xdx where x is any positive whole number. If you want to add or subtract from the result you can add +x or -x at the end.")
        input_text = get_input(":")
        pattern = re.compile(r"^(\d+)d(\d+)([+-]\d+)?$")
        match = pattern.search(input_text)
        pattern_num = re.compile(r"^(\d+)$")
        match_num = pattern_num.search(input_text)
        if match:
            result = roll(int(match.group(1)), int(match.group(2)))
            if match.group(3):
                result += int(match.group(3))
            print(f"Result of the roll: {result}")
            break
        elif match_num:
            result = int(input_text)
            break
        else:
            print("Wrong formatting, please try again (examples: 12, 1d4+2, 2d8).")
    return result

