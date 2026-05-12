class MovingAverage:

    def __init__(self, size: int):
        self.lst = []
        self.size = size
        self.left = 0
        self.curr_sum = 0
    
    def next(self, val: int) -> float:
        self.lst.append(val)
        self.curr_sum += val
        if len(self.lst) <= self.size:
            return self.curr_sum / len(self.lst)
        else:
            self.curr_sum -= self.lst[self.left]
            self.left += 1
            return self.curr_sum / self.size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)