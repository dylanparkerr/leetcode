'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max_ones = 0
    count = 0
    for num in nums:
        if(num == 1):
            count = count + 1
        else:
            count = 0
        max_ones = max(count, max_ones) 
    return max_ones


'''
Given an array nums of integers, return how many of them contain an even number of digits.
Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 105
'''
def evenDigits(self, num):
    digits = 0
    while num > 0:
        num //= 10  # floor division so it remains an integer
        digits += 1
    return digits % 2 == 0  # return if the number of digits is even

def findNumbers(self, nums: List[int]) -> int:
    count = 0
    for n in nums:
        count += self.evenDigits(n)  # ex: 1 + True = 2
    return count


'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
'''
    def sortedSquares(self, nums: List[int]) -> List[int]: