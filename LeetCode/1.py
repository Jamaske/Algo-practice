class Solution:
    TC = [
        ([2,7,11,15], 9),
        ([3,2,4], 6)
    ]

    """
    sort + two pointers
    time O(n*log(n))'
    space O(1) (inplace)
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = list(enumerate(nums))
        arr.sort(key = lambda pair: pair[1])
        i = 0
        j = len(nums) - 1 
        while i < j:
            s = arr[i][1] + arr[j][1]
            if s == target:
                break
            elif s < target:
                i += 1
            else:
                j -= 1

        return [arr[i][0], arr[j][0]]
    
    """
    reverse hash maping
    time O(1)
    space O(n)
    """
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        idxLookup = {}
        for i, num in enumerate(nums):
            compliment = target - num
            com_idx = idxLookup.get(compliment)
            if com_idx is not None:
                return [i, com_idx]
            else:
                idxLookup[num] = i
    """
    same
    +preallocate full dict at once
    -no early solutions befor first nums pass
    """
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
            idxLookup = {num:i for i,num in enumerate(nums)}
            
            for i, num in enumerate(nums):
                compliment = target - num
                com_idx = idxLookup.get(compliment)
                if com_idx is not None and com_idx != i:
                    return [i, com_idx]


if __name__ == "__main__":
    print(Solution().twoSum2(*Solution.TC[1]))