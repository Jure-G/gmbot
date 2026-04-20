This is a combat helper for game masters in TTRPG-s.
-   It tracks monster stats (stat block + current hp, current initiative, current spell slots, any condition it is under and 
    any special resources it may have)
-   It constructs initiative order and gives the gm the currently active character and it's stats.
-   It rolls some things automatically and asks for gm imput when necessary.

When combat starts it asks how many players there are, their names and their current initiative, imports NPC stats from a file, rolls inititative 
for them and constructs initiative order. 

Then it presents the first character in the initiative order, prints it's stats and asks you what to do.
options are MOVE, ATTACK, CAST SPELL, USE SPECIAL, ADD/REMOVE CONDITION, END TURN and REMOVE FROM FIGHT.
if it is a player it only prints the player name and conditions the player is under. The only options are ADD/REMOVE CONDITION, END TURN and
REMOVE FROM FIGHT.

whatever you choose to do, the program will do any rolls necessary, print them out and print out an updated stat block with removed resources.
if you END TURN or REMOVE FROM FIGHT the program goes to the next character in initiative order and do the same.


