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
        vowel_seen: bool = False
        consonant_seen: bool = False
        vowel_count: dict[str, int] = {}
        consonant_count: dict[str, int] = {}

        for c in s:
            if c in 'aeiou':
                vowel_seen = True
                vowel_count[c] = vowel_count.get(c, 0) + 1
            else:
                consonant_seen = True
                consonant_count[c] = consonant_count.get(c, 0) + 1

        if not vowel_seen and not consonant_seen:
            return 0
        if not vowel_seen:
            return max(consonant_count.values())
        if not consonant_seen:
            return max(vowel_count.values())
        return max(vowel_count.values()) + max(consonant_count.values())


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

