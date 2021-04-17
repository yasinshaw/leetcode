#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # 边界,最开始的边界在外面
        left, top, right, bottom = -1, -1, len(matrix[0]), len(matrix)
        # 方向增量
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # 当前方向
        cur_direction = 0
        # 用i, j来表示当前遍历到的位置, 触发到边界就转向，每次i, j的增量为direction
        i, j = 0, 0
        while left < j < right and top < i < bottom:
            x, y = directions[cur_direction][0], directions[cur_direction][1]
            result.append(matrix[i][j])
            ## 达到边界，转向，并缩小边界 这里看代码能不能优化下
            if i + x == top or i + x == bottom or j + y == left or j + y == right:
                if cur_direction == 0:
                    top += 1
                if cur_direction == 1:
                    right -= 1
                if cur_direction == 2:
                    bottom -= 1
                if cur_direction == 3:
                    left += 1
                cur_direction = (cur_direction + 1) % 4
            # 这里变向了，所以xy重新计算
            x, y = directions[cur_direction][0], directions[cur_direction][1]
            i += x
            j += y
            # print(i, j, left, top, right, bottom, result)
        return result

# @lc code=end

