# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        self.weights = {}
        return self.getWeight(n)

    def getWeight(self, n: int) -> int:
        if n == 0:
            return 0
        if n not in self.weights:
            self.weights[n] = (1 & n) + self.getWeight(n >> 1)
        return self.weights[n]


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = 11
    print(a, sep=", ")
    print(sol.hammingWeight(a))

    print("--- CASE 2 ---")
    a = 128
    print(a, sep=", ")
    print(sol.hammingWeight(a))

    print("--- CASE 3 ---")
    a = 2147483645
    print(a, sep=", ")
    print(sol.hammingWeight(a))

