# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.
# 
# You are given an integer n, an array languages, and an array friendships where:
# 
# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.
# 
# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
#  
# 
# Example 1:
# 
# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:
# 
# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.

class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        friends_cannot_talk = set()

        for friends in friendships:
            can_communicate = False
            languages_of_first_friend = set(languages[friends[0] - 1])
            for language in languages[friends[1] - 1]:
                if language in languages_of_first_friend:
                    can_communicate = True
                    break
            if not can_communicate:
                friends_cannot_talk.add(friends[0] - 1)
                friends_cannot_talk.add(friends[1] - 1)

        max_already_know = 0
        already_know = [0] * (n + 1)
        for friend in friends_cannot_talk:
            for language in languages[friend]:
                already_know[language] += 1
                max_already_know = max(already_know[language], max_already_know)

        return len(friends_cannot_talk) - max_already_know


if __name__ == "__main__":
    sol = Solution()

    a = 2
    b = [[1], [2], [1, 2]]
    c = [[1, 2], [1, 3], [2, 3]]
    print("--- CASE 1 ---")
    print(a, b, c, sep=", ")
    print(sol.minimumTeachings(a, b, c))

    a = 3
    b = [[2], [1, 3], [1, 2], [3]]
    c = [[1, 4], [1, 2], [3, 4], [2, 3]]
    print("--- CASE 2 ---")
    print(a, b, c, sep=", ")
    print(sol.minimumTeachings(a, b, c))

