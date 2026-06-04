This is a combat helper for game masters in DND 5e.
-   It tracks monster stats (stat block + current hp, current initiative, current spell slots, any condition it is under and any rechargable abilities it may have)
-   It constructs initiative order and gives the gm the currently active character and it's stats.
-   It rolls some things automatically and asks for gm imput when necessary.

When combat starts it asks how many players there are, their names and their current initiative, imports NPC stats from a file, rolls inititative for them and constructs the initiative order. 

Then it presents the first character in the initiative order, prints it's stats and asks you what to do.
options are ATTACK, HEAL, CAST SPELL, USE RECHARGABLE, ADD/REMOVE CONDITION, END TURN and ROLL.
if it is a player it only prints the player name and conditions the player is under. The only options are ATTACK, HEAL, ADD/REMOVE CONDITION, END TURN and ROLL.

- ATTACK x reduces hp of the target(x) by a specified amount
- HEAL x adds specified hp to the target(x)
- CAST SPELL reduces the amount of spell slots
- USE RECHARGABLE uses rechargable and flags it as used
- ADD/REMOVE CONDITION adds or removes condition you specify for amount of turns you specify
- END TURN goes to the next character in initiative
- ROLL xdx (where x is any positive intiger) + or - y (where y is any intiger) simulates rolling x times dx tice and adding and subtracting y ex. 2d6+3 (adds two random numbers from 1 to 6 (including both) plus 3)

statblocks.txt is an example of how statblocks must be written to get imported properly.
before every statblock there must be a num = *number of same stat blocks you want included*
directly under it there must be a stat block formatted as if you copied and pasted it from https://www.5esrd.com
