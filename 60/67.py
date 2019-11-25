class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) <= len(b):
            s = a[::-1]
            t = b[::-1]
        else:
            s = b[::-1]
            t = a[::-1]

        result = list(t)
        flag = 0
        for i in range(len(t)):
            if i < len(s):
                si = s[i]
            else:
                si = '0'

            if flag:
                if si == '1':
                    # flag = 1, t[i] = t[i]
                    pass
                else:
                    if t[i] == '1':
                        result[i] = '0'
                        flag = 1
                    else:
                        result[i] = '1'
                        flag = 0
            else:
                if si == '1' and t[i] == '1':
                    flag = 1
                    result[i] = '0'
                elif si == '1' or t[i] == '1':
                    result[i] = '1'
                else:
                    result[i] = '0'

        if flag: result.append('1')
        return ''.join(result[::-1])


a = "1010"
b = "1011"

s = Solution()
x = s.addBinary(a, b)
print(x)