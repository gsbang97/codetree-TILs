class Agent:
    def __init__(self, t):
        code, score = t
        self._code = code
        self._score = int(score)
    def __str__(self):
        return f'{self._code} {self._score}'
    def getScore(self):
        return self._score
    
agents = [ Agent(input().split()) for _ in range(5) ]

agents.sort(key = lambda agent : agent.getScore())

print(agents[0])