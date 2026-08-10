class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Initialize two pointers at opposite ends of the array
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            # If the target is found, return 1-based indices
            if current_sum == target:
                return [left + 1, right + 1]
            
            # If current sum is too small, move the left pointer to increase the sum
            elif current_sum < target:
                left += 1
                
            # If current sum is too large, move the right pointer to decrease the sum
            else:
                right -= 1
