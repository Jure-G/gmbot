import re
import random
from helpers import get_input, roll
from import_data import import_data
from commands import roll_command, damage, heal, conditions, spellslots

def main():
    print("Welcome to GMbot! If you at any point want to exit the program you can write exit or q.")
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
                #print conditions if the creature is under any
                if len(active_creature["conditions"]) > 0:
                    print(f"Current conditions and how many rounds they are active: {active_creature["conditions"]}")
                while True:
                    print(f"What will {active_creature["name"]} do?")
                    print("Commands: (d)amage, (h)eal, add/remove (c)onditions, (r)oll, (e)nd turn")
                    command = get_input(":")
                    #attack 
                    if command.lower() == "d":
                        damage(creatures)
                    #heal 
                    elif command.lower() == "h":
                        heal(creatures)
                    #conditions
                    elif command.lower() == "c":
                        conditions(creatures)
                    #roll
                    elif command.lower() == "r":
                        roll_command()
                    #end turn
                    elif command.lower() == "e":
                        break
                    else:
                        print("Incorrect command.")
                        continue
                for condition in active_creature["conditions"]:
                    active_creature["conditions"][condition] += 1
            #menu for NPCs
            else:
                print("Active:")
                for line in active_creature["statblock"]:
                    print(line)
                #print conditions if the creature is under any
                if len(active_creature["conditions"]) > 0:
                    print(f"Current conditions and how many rounds they are active: {active_creature["conditions"]}")
                #if creature has a rechargable abilty, check if it is avaliable and print it, if not avaliable roll for recharge and print the result
                if len(active_creature["rechargable"]) > 0:
                    rechargable = active_creature["rechargable"]
                    if rechargable["is_avaliable"]:
                        print(f"Rechargable ablity {rechargable["name"]} is ready for use.")
                    else:
                        print(f"Rolling 1d{rechargable["max"]} for recharge of {rechargable["name"]}.")
                        result = roll(1, rechargable["max"])
                        print(f"Result: {result}")
                        if result >= rechargable["min"]:
                            rechargable["is_avaliable"] = True
                            print(f"{active_creature["name"]} recharges {rechargable["name"]}.")
                        else:
                            print(f"{active_creature["name"]} doesn't recharge {rechargable["name"]}.")
                while True:
                    print(f"What will {active_creature["name"]} do?")
                    print("Commands: (d)amage, (h)eal, add/remove (c)onditions, use (s)pell slot, mark rechargable (a)bility as used, (r)oll, (e)nd turn")
                    command = get_input(":")
                    #attack
                    if command.lower() == "d":
                        damage(creatures)
                    #heal
                    elif command.lower() == "h":
                        heal(creatures)
                    #conditions
                    elif command.lower() == "c":
                        conditions(creatures)
                    #spells
                    elif command.lower() == "s":
                        spellslots(active_creature)
                    #rechargable ability
                    elif command.lower() == "a":
                        if active_creature["rechargable"]["is_avaliable"]:
                            print("Rechargable abilty marked as used")
                            active_creature["rechargable"]["is_avaliable"] = False
                        else:
                            print("Rechargable not avaliable to use")
                    #roll
                    elif command.lower() == "r":
                        roll_command()
                    #end turn
                    elif command.lower() == "e":
                        break
                    else:
                        print("Incorrect command.")
                        continue
                for condition in active_creature["conditions"]:
                    active_creature["conditions"][condition] += 1
        round += 1

if __name__ == "__main__":
    main()
