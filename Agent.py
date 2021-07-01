class Agent:
    def __init__(self, cost, synergies):
        self.cost = cost
        self.synergies = synergies

    def __str__(self):
        return f"{self.__class__.__name__}"# - cost: {self.cost}"

    def __repr__(self):
        return str(self)

