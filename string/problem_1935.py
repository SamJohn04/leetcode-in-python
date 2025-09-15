# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
# 
# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")

        count = 0
        for word in words:
            for c in word:
                if c in brokenLetters:
                    break
            else: # Only runs if no break was called
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = "hello world"
    b = "ad"
    print(a, b, sep=", ")
    print(sol.canBeTypedWords(a, b))

    print("--- CASE 2 ---")
    a = "leet code"
    b = "lt"
    print(a, b, sep=", ")
    print(sol.canBeTypedWords(a, b))

    print("--- CASE 3 ---")
    a = "leet code"
    b = "e"
    print(a, b, sep=", ")
    print(sol.canBeTypedWords(a, b))

