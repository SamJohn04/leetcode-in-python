# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set(nums)
        return len(numSet) != len(nums)


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = [1, 2, 3, 1]
    print(a, sep=", ")
    print(sol.containsDuplicate(a))

    print("--- CASE 2 ---")
    a = [1,2,3,4]
    print(a, sep=", ")
    print(sol.containsDuplicate(a))

    print("--- CASE 3 ---")
    a = [1,1,1,3,3,4,3,2,4,2]
    print(a, sep=", ")
    print(sol.containsDuplicate(a))

