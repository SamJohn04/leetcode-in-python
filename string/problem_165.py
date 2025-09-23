# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
# 
# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
# 
# Return the following:
# 
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        firstVersion = [int(v) for v in version1.split(".")]
        secondVersion = [int(v) for v in version2.split(".")]

        while len(firstVersion) < len(secondVersion):
            firstVersion.append(0)
        while len(firstVersion) > len(secondVersion):
            secondVersion.append(0)

        for i in range(len(firstVersion)):
            if firstVersion[i] < secondVersion[i]:
                return -1
            elif firstVersion[i] > secondVersion[i]:
                return 1

        return 0


if __name__ == "__main__":
    sol = Solution()

    print("--- CASE 1 ---")
    a = "1.2"
    b = "1.10"
    print(a, b, sep=", ")
    print(sol.compareVersion(a, b))

    print("--- CASE 2 ---")
    a = "1.01"
    b = "1.001"
    print(a, b, sep=", ")
    print(sol.compareVersion(a, b))

    print("--- CASE 3 ---")
    a = "1.0"
    b = "1.0.0.0"
    print(a, b, sep=", ")
    print(sol.compareVersion(a, b))

