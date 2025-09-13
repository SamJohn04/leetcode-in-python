# Alice and Bob are playing a game on a string.
# 
# You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:
# 
# On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels.
# On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels.
# The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.
# 
# Return true if Alice wins the game, and false otherwise.
# 
# The English vowels are: a, e, i, o, and u.

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # This one seems random, so let me explain.
        # Let's just say there are 3 scenarios:
        # Scenario 1: There are an odd number of vowels. In this case, Alice takes the whole string, and she wins.
        # Scenario 2: There are an even number of vowels (except 0). In this case,Alice takes a substring an odd number of vowels.
        #   There remains an odd number of vowels. Bob takes an even number, and Alice takes the rest, and she wins.
        # Scenario 3: There are no vowels. In this case, Alice automatically loses.

        # Therefore, the question becomes "Does the string have vowel(s) in it?", which I have solved beow.
        for c in 'aeiou':
            if c in s:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = "leetcoder"
    print(a, sep=", ")
    print(sol.doesAliceWin(a))

    print("--- CASE 2 ---")
    a = "bbcd"
    print(a, sep=", ")
    print(sol.doesAliceWin(a))

