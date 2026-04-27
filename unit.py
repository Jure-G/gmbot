

class Unit:
    def __init__(self, name):
        self.name = name
        self.initiative = 20


class Pc(Unit):
    def __init__(self, name, initiative):
        super().__init__(name)
        self.initiative = initiative

class Npc(Unit):
    def __init__(self, name, initiative, max_hp, speed, statblock):
        super().__init__(name)
        self.initiative = initiative
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.speed = speed
        self.statblock = statblock


    def take_damage(self, damage):
        if isinstance(damage, int) == False or damage < 0:
            print("Damage has to be a whole number.")
            return

        self.current_hp -= damage
        print(f"{self.name} takes {damage} damage.") 
        
        if self.current_hp >= 0:
            print(f"{self.name} currently has {self.current_hp} hp")
        else:
            self.current_hp = 0
            print(f"{self.name} dies.")
    
    def heal(self, healing):
        if isinstance(healing, int) == False or healing < 0:
            print("Healing has to be a whole number.")
            return

        if self.current_hp >= self.max_hp:
            print("Target is already at max hp")
            return

        self.current_hp += healing

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

        print(f"{self.name} currently has {self.current_hp} hp")


