class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == '':
            return s2 == s3
        elif s2 == '':
            return s1 == s3
        else:
            pass

        flag = False
        if flag == False and s1[0] == s3[0]:
            flag = self.isInterleave(s1[1:], s2, s3[1:])

        if flag == False and s2[0] == s3[0]:
            flag = self.isInterleave(s1, s2[1:], s3[1:])

        return flag




s1 = "aabc"
s2 = "dbbca"
s3 = "aadbbcbca"

# s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

print(len(s1), len(s2), len(s3))
solution = Solution()
x = solution.isInterleave(s1, s2, s3)
print(x)