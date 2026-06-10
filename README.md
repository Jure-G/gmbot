This is a combat helper for game masters in DND 5e.
-   It tracks monster stats (stat block + current hp, current initiative, current spell slots, any condition it is under and for how long it has been active and any rechargable abilities it may have)
-   It constructs initiative order and gives the gm the currently active character and it's stats.

When combat starts it asks to enter the player names and their rolled initiative, imports NPC stats from a file, rolls inititative for them and constructs the initiative order. 

Then it presents the first character in the initiative order, prints it's stats and asks you what to do.

- ATTACK x reduces hp of the target(x) by a specified amount
- HEAL x adds specified hp to the target(x)
- USE SPELLSLOT asks for the level of the spellslot and reduces the amount left by 1
- USE RECHARGABLE uses rechargable and flags it as used
- ADD/REMOVE CONDITION adds or removes condition you specify.
- END TURN goes to the next character in initiative
- ROLL asks for input of what you want to roll in standard format (ex. 1d4 rolls one 4 sided die, 2d20+3 rolls two 20 sided dies and adds 3 to it...)

statblocks.txt is an example of how statblocks must be written to get imported properly.
before every statblock there must be a line that only includes the following: num = x (where x is the number of times the same creature repeats itself)
directly under it there must be a stat block formatted as if you copied and pasted it from https://www.5esrd.com
