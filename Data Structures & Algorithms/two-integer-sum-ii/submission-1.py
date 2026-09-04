class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            sol = numbers[left] +numbers[right]
            if sol == target:
                return [left + 1, right + 1]
            elif sol < target:
                left += 1
            else:
                right -= 1

                
        