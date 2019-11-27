class Solution(object):
    def lineWords(self, line, maxWidth):
        width = 0
        count = len(line) - 1
        for w in line:
            width += len(w)

        if count == 0:
            s = line[0]
            s += ' ' * (maxWidth - width)
            return s

        blankCount, remain = (maxWidth - width) // count, (maxWidth - width) % count
        # print(line, blankCount, remain)

        s = ''
        for i in range(count):
            s += line[i]
            s += ' ' * blankCount
            if remain > 0:
                s += ' '
                remain -= 1

        s += line[-1]
        return s

    def lastLine(self, line, maxWidth):
        s = line[0]
        for i in range(1, len(line)):
            s += ' ' + line[i]

        width = len(s)
        s += ' ' * (maxWidth - width)
        return s


    def wordSplit(self, words, maxWidth):
        result = []
        start = 0
        end = 0

        length = len(words)
        width = 0
        while end < length:
            l = len(words[end])
            if width + l <= maxWidth:
                width += l + 1
            else:
                result.append(words[start:end])
                start = end
                width = l + 1
            end += 1
        if start < end:
            result.append(words[start:end])

        return result

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        split = self.wordSplit(words, maxWidth)

        result = []
        for i in range(len(split)-1):
            line = self.lineWords(split[i], maxWidth)
            result.append(line)

        lastLine = self.lastLine(split[-1], maxWidth)
        result.append(lastLine)

        return result




words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16


solution = Solution()
x = solution.fullJustify(words, maxWidth)
print(x)