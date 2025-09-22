# You are given a string s consisting of lowercase English letters ('a' to 'z').
# 
# Your task is to:
# 
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.
# 
# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
# 
# The frequency of a letter x is the number of times it occurs in the string.

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelSeen: bool = False
        consonantSeen: bool = False
        vowelCount: dict[str, int] = {}
        consonantCount: dict[str, int] = {}

        for c in s:
            if c in 'aeiou':
                vowelSeen = True
                vowelCount[c] = vowelCount.get(c, 0) + 1
            else:
                consonantSeen = True
                consonantCount[c] = consonantCount.get(c, 0) + 1

        if not vowelSeen and not consonantSeen:
            return 0
        if not vowelSeen:
            return max(consonantCount.values())
        if not consonantSeen:
            return max(vowelCount.values())
        return max(vowelCount.values()) + max(consonantCount.values())


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = "successes"
    print(a, sep=", ")
    print(sol.maxFreqSum(a))

    print("--- CASE 2 ---")
    a = "aeiaeia"
    print(a, sep=", ")
    print(sol.maxFreqSum(a))

