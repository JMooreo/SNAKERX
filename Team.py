from Synergy import allSetBonuses

class Team:
    def __init__(self, agents):
        self.agents = agents
        self.synergies = self.get_synergies()
        self.score = self.get_score()

    def __str__(self):
        return f"{self.agents}\n{self.synergies}"
    
    def get_synergies(self):
        synergies = {}

        for key in [synergy for agent in self.agents for synergy in agent.synergies]:
            synergies[key] = synergies.get(key, 0) + 1

        return synergies

    def get_score(self):
        return sum([setBonus.get_bonus_level_achieved(self.synergies) for setBonus in allSetBonuses]) + sum([agent.cost for agent in self.agents])

