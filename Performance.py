import time

class Performance:
    def __init__(self):
        self.t0 = 0
        self.t1 = 0

    def start_timing(self):
        self.__init__()
        self.t0 = time.perf_counter()

    def stop_timing(self):
        self.t1 = time.perf_counter()

    def get_diff(self):
        return self.t1 - self.t0
