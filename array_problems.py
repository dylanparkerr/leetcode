'''
Arrays:
Standard implementations normally have a fixed length. However, they can have be
implemtented in a way that allows them to grow and shrink dynamically.

Different languages assign different values for initiallized but unassigned indexes
in arrays. The initialization value will also depend on the object type stored in
the array.

Insertion has an average time of O(n), where n is the number of items in the array.
This is because every element after the insertion point has to be moved over fist.



'''

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

Example:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Notes:
After squaring the numbers, the negatives will be removed, leaving the numbers unsorted. Then we
notice that the magnitude of the numbers are large on either end and slop inward. We can solve
this problem with two pointers, starting at the left and right, then compare the squares at each
pointer to see which to add to the list. This solution is fast at O(1) time since sorting is 
accomplished as we move each element.

Visualisation of [r-l] appending from the right side of array:
https://pythontutor.com/visualize.html#code=def%20sortedSquares%28A%29%3A%0A%20%20%20%20answer%20%3D%20%5B0%5D%20*%20len%28A%29%0A%20%20%20%20l,%20r%20%3D%200,%20len%28A%29%20-%201%0A%20%20%20%20while%20l%20%3C%3D%20r%3A%0A%20%20%20%20%20%20%20%20left,%20right%20%3D%20abs%28A%5Bl%5D%29,%20abs%28A%5Br%5D%29%0A%20%20%20%20%20%20%20%20if%20left%20%3E%20right%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20answer%5Br%20-%20l%5D%20%3D%20left%20*%20left%0A%20%20%20%20%20%20%20%20%20%20%20%20l%20%2B%3D%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20answer%5Br%20-%20l%5D%20%3D%20right%20*%20right%0A%20%20%20%20%20%20%20%20%20%20%20%20r%20-%3D%201%0A%20%20%20%20return%20answer%0A%20%20%20%20%0Anums%20%3D%20%5B-7,-6,-5,-2,2,3,11%5D%0A%0AsortedSquares%28nums%29&cumulative=false&curInstr=37&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''
def sortedSquares(self, nums: List[int]) -> List[int]:
    answer = [0] * len(nums)  # an array 'empty' array of 0's with the same length of nums
    l = 0  # left pointer
    r = len(nums) - 1  # right pointer
    while l <= r:
        left = abs(nums[l])
        right = abs(nums[r])
        if left > right:
            answer[r-l] = left * left  # see visualization 
            l += 1
        else:
            answer[r-l] = right * right
            r -= 1
    return answer


'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 9
'''
def duplicateZeros(self, arr: List[int]) -> None:
   print('todo') 
