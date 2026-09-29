class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i in range(self.n):
            self.add(i + 1, nums[i])

    def add(self, index, value):
        while index <= self.n:
            self.bit[index] += value
            index += index & -index

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, diff)

    def prefixSum(self, index):
        s = 0
        while index > 0:
            s += self.bit[index]
            index -= index & -index
        return s

    def sumRange(self, left, right):
        return self.prefixSum(right + 1) - self.prefixSum(left)