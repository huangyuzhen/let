#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *longestPalindrome(char *str)
{
    int length = strlen(str);
    char *result = malloc(length + 1);
    result[0] = '\0';

    int maxL = 0;
    // 枚举k，枚举值为回文字符串中心的位置, O(n^2)
    for (int k = 0; k < length; k++)
    {
        char *center = str + k;
        char *s = center;
        char *t = center;

        // center为中心,尽量向右扩展,单向扩展即可,并且如果发生扩展，那么可以优化k,k++直接向前一步,
        while (t < str + length && *(t + 1) == *center)
        {
            k++;
            t++;
        }
        // 同时向两边扩展,s向左，t向右
        while (s > str && t < str + length && *(s - 1) == *(t + 1))
        {
            s--;
            t++;
        }
        // 结果处理
        int sLen = t - s + 1;
        if (sLen > maxL)
        {
            maxL = sLen;
            strncpy(result, s, sLen);
            result[sLen] = '\0';
        }
    }

    return result;
}

int main()
{
    char s[] = "babad";
    char *t = longestPalindrome(s);
    printf("%s\n", t);
    return 0;
}