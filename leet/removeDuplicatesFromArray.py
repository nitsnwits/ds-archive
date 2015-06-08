# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# remove duplicates from sorted array
# class Solution:
    # @param {integer[]} nums
    # @return {integer}
def removeDuplicates(nums):
    lenOfNums = len(nums)
    if lenOfNums <= 1:
        return lenOfNums
    newIdx = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        nums[newIdx + 1] = nums[i]
        newIdx += 1
    return newIdx + 1

print removeDuplicates([0,0,0,0,0])
print removeDuplicates([1,2,3,4,5])
print removeDuplicates([1,1,3,4,5])