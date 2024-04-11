from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    complement_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in complement_dict:
            return [complement_dict[complement], i]
        complement_dict[num] = i
    return []
"""
def main():
    nums = []
    while True:
        num_str = input("Enter a number (or leave a blank to finish!): ")
        if num_str.strip() == "":
            break
        num = int(num_str)
        nums.append(num)
    target = int(input("Enter the target sum: "))

    result = twoSum(nums, target)
    print(result)
    
if __name__ == "__main__":
    main()
"""