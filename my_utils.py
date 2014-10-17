import time
from collection import defaultdict


class StopClock(object):
    """An object for profiling code"""
    def __init__(self):
        self.checkpoints = []
        self.checkpoint_names = []
        self.time_accumulator = defaultdict(float)
        self.accumulator_starts = defaultdict(float)

    def checkpoint(self, name):
        self.checkpoints.append(time.time())
        self.checkpoint_names.append(name)

    def get_checkpoints(self):
        deltas = [b - a for a, b in zip(self.checkpoints, self.checkpoints[1:])]
        for row in zip(self.checkpoint_names[1:], deltas):
            yield row

    def print_checkpoints(self):
        for row in self.get_checkpoints():
            print row

    def start_accumulate(self, name):
        self.accumulator_starts[name] = time.time()

    def stop_accumulator(self, name):
        assert name in self.accumulator_starts
        self.time_accumulator[name] += (time.time() - self.accumulator_starts[name])

    def print_accumulator(self):
        for event, time_taken in self.time_accumulator.iteritems():
            print (event, time_taken)


if __name__ == '__main__':
    a = StopClock()
    a.checkpoint('start')
    time.sleep(1)
    a.checkpoint('b')
    time.sleep(2)
    a.checkpoint('c')
    time.sleep(1.5)
    a.checkpoint('d')
    time.sleep(1)
    a.checkpoint('g')
    a.print_checkpoints()
    a.start_accumulate('three')
    time.sleep(1)
    a.stop_accumulator('three')
    a.start_accumulate('one')
    time.sleep(1)
    a.stop_accumulator('one')
    a.start_accumulate('three')
    time.sleep(1)
    a.stop_accumulator('three')
    a.start_accumulate('three')
    time.sleep(1)
    a.stop_accumulator('three')
    a.print_accumulator()
