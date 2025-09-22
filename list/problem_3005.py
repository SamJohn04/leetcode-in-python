# You are given an array nums consisting of positive integers.
# 
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# 
# The frequency of an element is the number of occurrences of that element in the array.

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        numsDict = {}
        for n in nums:
            numsDict[n] = numsDict.get(n, 0) + 1

        count = 0
        highest = 0
        for val in numsDict.values():
            if val == highest:
                count += 1
            elif val > highest:
                count = 1
                highest = val

        return count * highest


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = [1,2,2,3,1,4]
    print(a, sep=", ")
    print(sol.maxFrequencyElements(a))

    print("--- CASE 2 ---")
    a = [1,2,3,4,5]
    print(a, sep=", ")
    print(sol.maxFrequencyElements(a))

