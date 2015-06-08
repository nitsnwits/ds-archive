# https://leetcode.com/problems/contains-duplicate-ii/
# Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} k
#     # @return {boolean}


def containsNearbyDuplicate(nums, k):
	if len(nums) <= 1:
		return False
	if k >= len(nums):
		k = len(nums) - 1
	for i in range(len(nums) - k):
		for j in range(i + 1, i + k + 1):
			if nums[i] == nums[j]:
				return True
	return False

print containsNearbyDuplicate([1,1], 1)
print containsNearbyDuplicate([1,2,3,1],2)
print containsNearbyDuplicate([],1)
print containsNearbyDuplicate([99, 99], 2)
print containsNearbyDuplicate([1],1)
print containsNearbyDuplicate([1,2],2)
        