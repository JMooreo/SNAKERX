import math

class SetBonus:
    def __init__(self, synergy, num_levels, level_cost):
        self.synergy = synergy
        self.num_levels = num_levels
        self.level_cost = level_cost

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return str(self)

    def get_bonus_level_achieved(self, synergies):
        return synergies.get(self.synergy, 0) // self.level_cost

class RogueSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Rogue", 2, 3)

class NukerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Nuker", 2, 3)

class RangerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Ranger", 2, 3)

class HealerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Healer", 2, 2)

class MageSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Mage", 2, 3)

class EnchanterSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Enchanter", 2, 2)

class SorcererSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Sorcerer", 3, 2)

class WarriorSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Warrior", 2, 3)

class ForcerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Forcer", 2, 2)

class MercenarySetBonus(SetBonus):
    def __init__(self):
        super().__init__("Mercenary", 2, 2)

class ConjurerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Conjurer", 2, 2)

class SwarmerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Swarmer", 2, 2)

class CurserSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Curser", 2, 2)

class VoiderSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Voider", 2, 2)

class PsykerSetBonus(SetBonus):
    def __init__(self):
        super().__init__("Psyker", 1, 1)

allSetBonuses = [
    RogueSetBonus(),
    NukerSetBonus(),
    RangerSetBonus(),
    HealerSetBonus(),
    MageSetBonus(),
    EnchanterSetBonus(),
    SorcererSetBonus(),
    WarriorSetBonus(),
    ForcerSetBonus(),
    # MercenarySetBonus(),
    ConjurerSetBonus(),
    SwarmerSetBonus(),
    CurserSetBonus(),
    VoiderSetBonus(),
    # PsykerSetBonus()
]
