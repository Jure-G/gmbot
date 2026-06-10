import re
from helpers import target_selection, input_roll, get_input

def roll_command():
    while True:
        print("Write the number of dice followed by the letter d and the size of the dice, if you would like to add or subtract something write it right after the size.")
        print("examples: 1d4, 2d8+4, 10d100-50")
        user_input = get_input(":")
        result = input_roll(user_input)
        if result:
            break
def damage(creatures):
    print("Attacking!")
    target = target_selection(creatures)
    while True:
        print("If you would like to roll for damage write the number of dice followed by the letter d and the size of the dice, if you would like to add or subtract something write it right after the size. You can also just write the final number.")
        print("examples: 1d4, 2d8+4, 10d100-50, 20")
        damage_input = get_input(":")
        damage = input_roll(damage_input)
        if damage:
            break
        
    #reduce the current_hp of the target by damage
    if target["type"] == "NPC":
        target["current_hp"] -= damage
        if target["current_hp"] <= 0:
            print(f"{target["name"]} died, leftover damage = {target["current_hp"]}.")
            target["current_hp"] = 0
            target["is_alive"] = False
        else:
            print(f"{target["name"]} took {damage} damage. HP left:{target["current_hp"]} / {target["max_hp"]}")
    else:
        print(f"{target["name"]} takes {damage} damage, make sure they mark it!")

def heal(creatures):
    print("Healing!")
    target = target_selection(creatures)
    while True:
        print("If you would like to roll for healing write the number of dice followed by the letter d and the size of the dice, if you would like to add or subtract something write it right after the size. You can also just write the final number.")
        print("examples: 1d4, 2d8+4, 10d100-50, 20")
        heal_input = get_input(":")
        heal = input_roll(heal_input)
        if damage:
            break
    #increase the targets health by heal amount
    if heal < 1:
        heal = 1
    if target["type"] == "NPC":
        if not target["is_alive"]:
            while True:
                print("The target is dead, does this heal revive it?")
                answer = get_input("(y)es, (n)o")
                if answer.lower() == "y":
                    target["current_hp"] = heal
                    if target["current_hp"] >= target["max_hp"]:
                        print(f"{target["name"]} is full hp.")
                        target["current_hp"] = target["max_hp"]
                        break
                    else:
                        print(f"{target["name"]} heals to {target["current_hp"]}.")
                        target["is_alive"] = True
                        break
                if answer.lower() == "n":
                    print("The target stays dead, heal is wasted.")
                    break
        else:
            target["current_hp"] += heal
            if target["current_hp"] >= target["max_hp"]:
                print(f"{target["name"]} is full hp.")
                target["current_hp"] = target["max_hp"]
            else:
                print(f"{target["name"]} heals to {target["current_hp"]}.")
    else:
        print(f"{target["name"]} heals for {heal} hp, make sure they mark it!")

def conditions(creatures):
    while True:
        print("Editing conditions.")
        target = target_selection(creatures)
        while True:
            print(target["name"])
            print(f"Current conditions and how many rounds they are active:{target["conditions"]}")
            print("commands:(a)dd, (r)emove or (s)top")
            command = get_input(":")
            if command.lower() == "a":
                print("Write the condition")
                user_input = get_input(":")
                target["conditions"][user_input] = 0
            elif command.lower() == "r":
                if len(target["conditions"]) < 1:
                    print(f"{target["name"]} has no active conditions.")
                    continue
                print(f"Current conditions:{target["conditions"]}")
                user_input = get_input("Write the name of the condition you would like to remove:")
                if user_input.lower() in target["conditions"]:
                    del target["conditions"][user_input.lower()]
                else:
                    print(f"{user_input.lower()} doesn't exist")

            elif command.lower() == "s":
                break
            else:
                print("Incorrect command, try again.")
        break_lower = False        
        while True:
            print("Do you want to target another creature?")
            print("Commands: (y)es (n)o")
            command = get_input(":")
            if command.lower() == "y":
                break
            elif command.lower() == "n":
                break_lower = True
                break
            else:
                print("Incorrect command.")
        if break_lower:
            break
        
def spellslots(active_creature):
    if len(active_creature["spellslots"]) < 1:
        print(f"{active_creature["name"]} can't cast spells.")
    else:
        print(f"{active_creature["name"]} has following spellslots left:")
        for spell_level in active_creature["spellslots"]:
            print(f"{spell_level}:{active_creature["spellslots"][spell_level]}")
        while True:
            print("What is the level of the spell you are casting?")
            input_level = get_input(":")
            input_level = input_level.lower()
            if input_level in active_creature["spellslots"]:
                if active_creature["spellslots"][input_level] > 0:
                    active_creature["spellslots"][input_level] -= 1
                    print(f"{active_creature["name"]} used one {input_level} level spellslot")
                    break
                else:
                    print(f"Casting failed because {active_creature["name"]} doesn't have any {input_level} level spellslots left.")
                    break
            else:
                print("Incorrect input, please try again, possible options:")
                for spell_level in active_creature["spellslots"]:
                    print(spell_level)
