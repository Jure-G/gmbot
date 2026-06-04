#Imports statblocks and returns a list of dictionaries containing npcs
import re

def import_data(path_to_file):
    with open(path_to_file) as f:
        statblocks = f.read()
    list_of_lines = statblocks.splitlines()
    num_nums = 0
    num_stats = 0

    #list of dictionaries that contain (index of statblock start, index of statblock end, number after "num =") 
    list_of_statblock_data = []

    line_i = 0
    for line in list_of_lines:
        pattern = re.compile(r"num \= (\d+)")
        match = pattern.search(line)
        pattern_stats = re.compile(r"(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))")
        match_stats = pattern_stats.search(line)
        if match:
            list_of_statblock_data.append({"start": line_i+1, "end": len(list_of_lines), "num": int(match.group(1))})
            num_nums += 1
        if match_stats:
            num_stats += 1
        line_i += 1
    
    #check for formatting errors
    if num_nums == 0 or num_stats == 0:
        raise Exception("No complete statblocks found")
    if num_nums != num_stats:
        raise Exception("Formatting error, number of num-s and statblocks is not equal")

    #set the end point in statblocks
    statblock_i = 1
    while statblock_i < len(list_of_statblock_data):
        list_of_statblock_data[statblock_i-1]["end"] = list_of_statblock_data[statblock_i]["start"] - 1
        statblock_i += 1

    statblock_list = []
    for statblock_data in list_of_statblock_data:
        i = 0
        while i < statblock_data["num"]:
            edited_lines = list_of_lines[statblock_data["start"]:statblock_data["end"]]
            if i > 0:
                edited_lines[0] = edited_lines[0] + " #" + str(i + 1)
            statblock_list.append(edited_lines)
                
            i += 1
    
    list_npcs = []

    for statblock in statblock_list:
        npc = {}
        #set type
        npc["type"] = "NPC"
        #set name
        npc["name"] = statblock[0]
        spell_slots = {}
        rechargable = {}
        #set empty list of conditions
        npc["conditions"] = {}
        formatted_statblock = []
        for line in statblock:
            #set rechargable
            pattern = re.compile(r"^\s*(.+)\s+\(Recharge (\d+-\d+)\)")
            match = pattern.search(line)
            if match:
                rechargable[match.group(1)] = match.group(2)

            #set spell_slots
            pattern = re.compile(r"(\d[st|nd|rd|th]+) level \((\d) slot")
            match = pattern.search(line)
            if match:
                spell_slots[match.group(1)] = int(match.group(2))

            #set max_hp and current_hp
            pattern = re.compile(r"Hit Points (\d+) \(\d+d\d+")
            match = pattern.search(line)
            if match:
                npc["max_hp"] = int(match.group(1))
                npc["current_hp"] = int(match.group(1))

            #set formatted statblock(list of lines) and initiative
            pattern = re.compile(r"STR\s+DEX\s+CON\s+INT\s+WIS\s+CHA")
            match = pattern.search(line)
            pattern_stats = re.compile(r"(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))\s+(\d+\s+\([+-]\d+\))")
            match_stats = pattern_stats.search(line)
            if match:
                continue
            elif match_stats:
                formatted_line = "STR = " + match_stats.group(1) + " DEX = " + match_stats.group(2) + " CON = " + match_stats.group(3) + " INT = " + match_stats.group(4) + " WIS = " + match_stats.group(5) + " CHA = " + match_stats.group(6)
                formatted_statblock.append(formatted_line)
                pattern_initiative = re.compile(r"\d+\s\(([+-]\d+)\)")
                match_initiative = pattern_initiative.search(match_stats.group(2))
                if match_initiative:
                        npc["initiative_bonus"] = match_initiative.group(1)
            else:
                formatted_statblock.append(line)
        npc["statblock"] = formatted_statblock
        npc["spell_slots"] = spell_slots
        npc["rechargable"] = rechargable
        npc["is_alive"] = True
        list_npcs.append(npc)
    return list_npcs
