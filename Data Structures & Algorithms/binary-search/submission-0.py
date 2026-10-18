class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            midpoint = (start + end) // 2
            
            if nums[midpoint] == target:
                return midpoint
            elif target > nums[midpoint]:
                start = midpoint + 1
            elif target < nums[midpoint]:
                end = midpoint - 1
                
        return -1