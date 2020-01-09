class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = []
        v2 = []
        for s in version1.split('.'):
            v1.append(int(s))
        for s in version2.split('.'):
            v2.append(int(s))

        flag = 1
        l1 = len(v1)
        l2 = len(v2)
        if l1 > l2:
            # 保证 l1 <= l2
            flag = -1
            v1, v2 = v2, v1
            l1, l2 = l2, l1

        i = 0
        while i < l1:
            if v1[i] < v2[i]:
                return -flag
            elif v1[i] > v2[i]:
                return flag
            i += 1

        while i < l2:
            if v2[i] > 0:
                return -flag
            i += 1

        return 0



version1 = "1.0"
version2 = "1"

sol = Solution()
x = sol.compareVersion(version1, version2)
print(x)