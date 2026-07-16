class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for num in range(len(numbers)):
            diff = target - numbers[num]
            if diff in hashMap:
                return [hashMap[diff], num + 1]
            hashMap[numbers[num]] = num + 1
        return []
        