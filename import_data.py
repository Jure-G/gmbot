#Imports statblocks and returns a list of dictionaries containing everything you need to create an appropriate amount of NPC objects
#name, initiative, max_hp, speed, statblock

def import_data(path_to_file):
    with open(path_to_file) as f:
        statblocks = f.read()
    list_of_lines = statblocks.splitlines()
    
    #list of dictionaries that contain (index of statblock start, index of statblock end, number after "num =") 
    list_of_statblock_data = []

    line_i = 0
    for line in list_of_lines:
        if "num =" in line:
            words = line.split()
            list_of_statblock_data.append({"start": line_i+1, "end": len(list_of_lines), "num": words[2]})
        line_i += 1

    #correct the end point in statblocks
    statblock_i = 0
    for statblock_data in list_of_statblock_data:
        if statblock_i == 0:
            statblock_i = 1
        else:
            list_of_statblock_data[statblock_i-1]["end"] = list_of_statblock_data[statblock_i]["start"] - 2
            statblock_i += 1
    



      


#only for testing, remove after done
import_data("./statblocks.txt")
