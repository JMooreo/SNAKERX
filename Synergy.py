from enum import Enum

class Synergy(Enum):
    Warrior = 1
    Ranger = 2
    Rogue = 3
    Mage = 4
    Sorcerer = 5
    Psyker = 6
    Healer = 7
    Enchanter = 8
    Nuker = 9
    Conjurer = 10
    Swarmer = 11
    Curser = 12
    Voider = 13
    Forcer = 14
    Mercenary = 15

    def __str__(self):
        return self.name

    def __repr(self):
        return str(self)

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
        try:
            return synergies[self.synergy] // self.level_cost
        except KeyError as e:
            return

        

class RogueSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Rogue, 2, 3)

class NukerSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Nuker, 2, 3)

class RangerSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Ranger, 2, 3)

class HealerSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Healer, 2, 2)

class MageSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Mage, 2, 3)

class EnchanterSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Enchanter, 2, 2)

class SorcererSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Sorcerer, 3, 2)

class WarriorSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Warrior, 2, 3)

class ForcerSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Forcer, 2, 2)

class MercenarySetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Mercenary, 2, 2)

class ConjurerSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Conjurer, 2, 2)

class SwarmerSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Swarmer, 2, 2)

class CurserSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Curser, 2, 2)

class VoiderSetBonus(SetBonus):
    def __init__(self):
        super().__init__(Synergy.Voider, 2, 2)

# class PsykerSetBonus(SetBonus):
#     def __init__(self):
#         super().__init__(Synergy.Psyker, 1, 1)

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
