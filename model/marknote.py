class Marknote:
    def __init__(self):
        self._marks = []

    def add(self, mark):
        self._marks.append(mark)

    def get(self, index):
        return self._marks[index]

    def size(self):
        return len(self._marks)

marknote = Marknote()

marknote.add(5)
marknote.add(10)
marknote.add(9)
marknote.add(8)

for mark in range(marknote.size()):
    print(marknote.get(index))