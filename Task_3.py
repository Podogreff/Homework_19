class Custom:
    def __init__(self, division, teams=None):
        self._division = division
        self._teams = teams

    def func(self, some):
        return some + "is a good team!"

    def __iter__(self):
        return (self.func(t) for t in self._teams)


team = Custom("Ukraine league", ["Dinamo", "Shahtar", "Niva"])


for i in team:
    print(i)

print(list(team))
