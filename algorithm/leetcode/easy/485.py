from typing import List

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    TARGET_NUMBER = 1
    count = 0
    max = 0

    for num in nums:
        if(num == TARGET_NUMBER):
            count += 1
        else:
            if(count > max):
                max = count
            count = 0
    
    if(count > max):
        max = count

    return max