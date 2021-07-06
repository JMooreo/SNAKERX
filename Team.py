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
        # Heavily score based on number of complete synergy levels,
        # But also factor in that higher cost units are better.
        # TODO: change scoring metric to be based on estimated damage per second.
        return sum(
            setBonus.get_bonus_level_achieved(self.synergies)
            for setBonus in allSetBonuses
        ) + 0.25 * sum(agent.cost for agent in self.agents)

