from typing import List

def shuffle(self, nums: List[int], n: int) -> List[int]:
    # n을 기준으로 두개의 리스트로 나눈다.
    x_array = nums[:n]
    y_array = nums[n:]

    # 하나씩 리스트를 합친다. 
    merged_array = []
    for x, y in zip(x_array, y_array):
        merged_array.append(x)
        merged_array.append(y)
    
    return merged_array