class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(32):
            if (n >> i) & 1:
                m =  m | (1 << (31-i))

        return m
