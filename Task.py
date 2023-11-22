from time import perf_counter

import numpy as np


class Task:
    def __init__(self, identifier, x, time=0, a=0, b=0, size=0):
        self.identifier = identifier
        self.a = a
        self.b = b
        self.x = x
        self.time = time

    def work(self, size: int) -> float:
        self.size = size
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size)

        start = perf_counter()
        np.linalg.solve(self.a, self.b)
        end = perf_counter()
        self.x = end - start

        return self.x


if __name__ == "__main__":
    task = Task(1, 2, 10)
    print(task.work(60))
