import re
import random
from helpers import get_input, input_roll
from import_data import import_data
from commands import attack, heal, conditions

def main():
    print("Wellcome to GMbot! If you at any point want to exit the program you can write exit or q.")
    path = get_input("Write the path to your statblock data file, if you wish to use default (./statblocks.txt) leave empty:")
    if path == "":
        creatures = import_data("./statblocks.txt")
    else:
        creatures = import_data(path)
    
    #roll initiative for NPCs
    for creature in creatures:
        creature["initiative"] = random.randrange(1, 21) + int(creature["initiative_bonus"])
    
    #add PCs
    print("Now we're going to add some player characters, you can add as many as you want. When you want to stop leave empty and press enter.")
    while True:
        name = get_input("Name: ")
        if name == "":
            break
        initiative = get_input("Rolled initiative: ")
        pattern = re.compile(r"([-+]\d+)|\d+")
        match = pattern.search(initiative)
        while not match:
            print("initiative must be an intiger")
            initiative = get_input("Rolled initiative: ")
            pattern = re.compile(r"([-+]\d+)|\d+")
            match = pattern.search(initiative)

        player = {}
        player["type"] = "PC"
        player["name"] = name
        player["initiative"] = initiative
        player["conditions"] = {}
        player["is_alive"] = True
        creatures.append(player)

    #construct initiative order
    def get_initiative(creature):
        return int(creature["initiative"])
    creatures.sort(key=get_initiative)
    round = 1

    #main loop, repeats initiative order untill the user exits
    while True:
        print(f"Round#{round}")
        #goes through the initiative order
        for active_creature in creatures:
            if not active_creature["is_alive"]:
                print(f"{active_creature["name"]} is dead, skipping...")
                continue
            #menu for PCs
            if active_creature["type"] == "PC":
                print(f"Active: {active_creature["name"]}")
                if len(active_creature["conditions"]) > 0:
                    print(f"Conditions it is under: {active_creature["conditions"]}")
                while True:
                    print(f"What will {active_creature["name"]} do?")
                    print("Commands: (a)ttack, (h)eal, add/remove (c)onditions, (r)oll, (e)nd turn")
                    command = get_input(":")
                    #attack 
                    if command.lower() == "a":
                        attack(creatures)
                    #heal 
                    elif command.lower() == "h":
                        heal(creatures)
                    #conditions
                    elif command.lower() == "c":
                        conditions(creatures)
                    #roll
                    elif command.lower() == "r":
                        result = input_roll()
                        print(result)
                    #end turn
                    elif command.lower() == "e":
                        break
                    else:
                        print("Incorrect command.")
                        continue
            #menu for NPCs
            else:
                print("Active:")
                for line in active_creature["statblock"]:
                    print(line)
                if len(active_creature["conditions"]) > 0:
                    print(f"Conditions it is under: {active_creature["conditions"]}")
                while True:
                    print(f"What will {active_creature["name"]} do?")
                    print("Commands: (a)ttack, (h)eal, add/remove (c)onditions, cast (s)pell, use (re)chargable, (r)oll, (e)nd turn")
                    command = get_input(":")
                    #attack
                    if command.lower() == "a":
                        attack(creatures)
                    #heal
                    elif command.lower() == "h":
                        heal(creatures)
                    #conditions
                    elif command.lower() == "c":
                        conditions(creatures)
                    #spells
                    elif command.lower() == "s":
                        pass
                    #rechargable
                    elif command.lower() == "re":
                        pass
                    elif command.lower() == "r":
                        result = input_roll()
                        print(result)
                    elif command.lower() == "e":
                        break
                    else:
                        print("Incorrect command.")
                        continue




        
        round += 1
        #still have to reduce time for conditions and remove them if 0 and roll for rechargable
if __name__ == "__main__":
    main()
