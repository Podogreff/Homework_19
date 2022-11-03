
class Range:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.index = 0

    def __iter__(self):
        return self

    # from smaller to bigger
    def __next__(self):
        if self.index + 1 >= self.stop:
            self.start -= self.index
            self.index = 0
            raise StopIteration
        num = self.start
        self.start += self.step
        self.index += self.step
        return num

    # from bigger to smaller
    # if self.stop >= self.start:
    #     self.start += self.index
    #     self.index = 0
    #     raise StopIteration
    # num = self.start
    # self.start -= self.step
    # self.index += self.step
    # return num


a = Range(1, 10)
b = Range(2, 23, 2)
c = Range(4, 43, 5)

print(list(a))
print(list(b))
print(list(c))
