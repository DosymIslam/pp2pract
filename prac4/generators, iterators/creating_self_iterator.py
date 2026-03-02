class MyNumbers:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_numbers = MyNumbers(5)

for num in my_numbers:
    print(num)