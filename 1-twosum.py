# coding:utf-8

"""
1. Two Sum [Array][Easy]
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
预期函数功能：给定一组整数，返回结果是一组两个索引，使数组索引对应的数值相加之和等于目标数值。
可以假设每个输入都有一个解决方案，并且保证给定数组中的元素不会出现两次。

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""


class Solution(object):

    def twoSum_TFM(self,nums, target):
        """
        我的思路： 从头开始，确定一个，后续遍历与之相加判断，设定一个temp_nums是为了区分没有遍历判断的剩余集合列表
        Runtime: 6565ms
        缺点: 线性思维，两层循环速度效率低
        """
        for i, i_num in enumerate(nums):
            temp_nums = nums[i + 1:]
            for j, j_num in enumerate(temp_nums):
                if i_num + j_num == target:
                    return[i, temp_nums.index(j_num) + i + 1]

    def twoSum_TSM(self, nums, target):
        """
        这是@jarrekk的答案
        我理解的思路: 1）把目标值和遍历元素值求差得出，得到另一个元素需要的理想值，有没有需要继续遍历判断。
                    2）建立temp_dict字典为存储求差值和其对应在暂未匹配元素的集合。
                    temp_dict和给定数组含有完整的元素集合，in去判定是因为经过差值计算得到预计元素值可能在之前遍历位置没匹配到，
                    所以要在temp_dict中进行判断存在否。
        """
        temp_dict = {}
        for i, i_num in enumerate(nums):
            if target-i_num in temp_dict:
                return[i, temp_dict[target - i_num]]
            temp_dict[i_num] = i
        return []

# if __name__ == '__main__':
#     test = Solution()
#     print(test.twoSum_TSM(nums=[1, 2, 3], target=5))
