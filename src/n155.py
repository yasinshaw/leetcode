#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minData = [math.inf] 


    def push(self, x: int) -> None:
        self.data.append(x)
        self.minData.append(min(x, self.minData[-1]))


    def pop(self) -> None:
        self.minData.pop()
        return self.data.pop()


    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.minData[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

