import re
from helpers import target_selection, input_roll, get_input

def attack(creatures):
    print("Attacking!")
    target = target_selection(creatures)
    damage = input_roll()
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
    heal = input_roll()
    #increase the targets health by heal amount
    if heal < 1:
        heal = 1
    if target["type"] == "NPC":
        if not target["is_alive"]:
            while True:
                print("The target is dead, does this heal revive it?")
                answer = get_input("(y)es, (n)o")
                if answer == "y":
                    target["current_hp"] = heal
                    if target["current_hp"] >= target["max_hp"]:
                        print(f"{target["name"]} is full hp.")
                        target["current_hp"] = target["max_hp"]
                        break
                    else:
                        print(f"{target["name"]} heals to {target["current_hp"]}.")
                        target["is_alive"] = True
                        break
                if answer == "n":
                    print("The target stays dead, heal is wasted.")
                    break
        else:
            target["current_hp"] += heal
            if target["current_hp"] >= target["max_hp"]:
                print(f"{target["name"]} is full hp.")
                target["current_hp"] = target["max_hp"]
            else:
                print(f"{target["name"]} heals to {target["current_hp"]}")
    else:
        print(f"{target["name"]} heals for {heal} hp, make sure they mark it!")

def conditions(creatures):
    while True:
        print("Editing conditions!")
        target = target_selection(creatures)
        while True:
            print(target["name"])
            print(f"Current conditions:{target["conditions"]}")
            print("commands:(a)dd, (r)emove or (s)top")
            command = get_input(":")
            if command.lower() == "a":
                while True:
                    print("Write the condition and the number of rounds it should stay in format: condition:number")
                    user_input = get_input(":")
                    pattern = re.compile(r"^(.+):(\d+)$")
                    match = pattern.search(user_input)
                    if match:
                        target["conditions"][match.group(1).lower()]=int(match.group(2))
                        break
                    else:
                        print("incorrect formatting, try again(ex. stun:2)")
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
                print("Incorrect command, try again")
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
                print("Incorrect command")
        if break_lower:
            break
        

