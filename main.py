from import_data import import_data
import random

def main():
    print("Wellcome to GMbot!")
    path = input("Write the path to your statblock data file, if you wish to use default (./statblocks.txt) leave empty:")
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
        name = input("Name: ")
        if name == "":
            break
        initiative = input("Rolled initiative: ")
        player = {}
        player["type"] = "PC"
        player["name"] = name
        player["initiative"] = initiative
        player["conditions"] = []
        creatures.append(player)

    #construct initiative order
    def get_initiative(creature):
        return int(creature["initiative"])
    creatures.sort(key=get_initiative)


if __name__ == "__main__":
    main()
