'''给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。'''

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''维护指针p0用来交换0，p1用来交换1，遍历数组
        如果遇到1，则与p1交换，然后p1右移一步
        如果遇到0，则与p0交换，然后p0和p1都右移一步。但如果p0 < p1，说明现在p0的位置上被换走的是之前换来的1，需要再换到p1处'''

        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0 :
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1 :
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1
            elif nums[i] == 1 :
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)