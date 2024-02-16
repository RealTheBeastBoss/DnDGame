from game import *

class Armour:
    def __init__(self, name, cost, ac, level, metal = False, stealth = False, strength = None):
        self.name = name
        self.cost = cost
        self.strengthDC = strength
        self.stealthDis = stealth
        self.type = level
        self.isMetal = metal
        self.baseArmourClass = ac
class Padded(Armour):
    def __init__(self):
        super().__init__("Padded Armour", 500, 11, ArmourType.LIGHT, False, True)
class Leather(Armour):
    def __init__(self):
        super().__init__("Leather Armour", 1000, 11, ArmourType.LIGHT)
class Studded(Armour):
    def __init__(self):
        super().__init__("Studded Leather Armour", 4500, 12, ArmourType.LIGHT)
class Hide(Armour):
    def __init__(self):
        super().__init__("Hide Armour", 1000, 12, ArmourType.MEDIUM)
class ChainShirt(Armour):
    def __init__(self):
        super().__init__("Chain Shirt", 5000, 13, ArmourType.MEDIUM, True)
class ScaleMail(Armour):
    def __init__(self):
        super().__init__("Scale Mail", 5000, 14, ArmourType.MEDIUM, False, True)
class Breastplate(Armour):
    def __init__(self):
        super().__init__("Breastplate", 40000, 14, ArmourType.MEDIUM, True)
class HalfPlate(Armour):
    def __init__(self):
        super().__init__("Half Plate Armour", 75000, 15, ArmourType.MEDIUM, True, True)
class RingMail(Armour):
    def __init__(self):
        super().__init__("Ring Mail", 3000, 14, ArmourType.HEAVY, True, True)
class ChainMail(Armour):
    def __init__(self):
        super().__init__("Chain Mail", 7500, 16, ArmourType.HEAVY, True, True, 13)
class Splint(Armour):
    def __init__(self):
        super().__init__("Splint Armour", 20000, 17, ArmourType.HEAVY, True, True, 15)
class Plate(Armour):
    def __init__(self):
        super().__init__("Plate Armour", 150000, 18, ArmourType.HEAVY, True, True, 15)