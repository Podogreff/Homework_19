
class WithIndex:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            self.start -= self.index
            self.index = 0
            raise StopIteration
        else:
            num = self.start
            letter = self.iterable[self.index]
            self.index += 1
            self.start += 1
            return num, letter


text = "hello"
new = WithIndex(text, 10)
for i in new:
    print(i)

print(list(new))

