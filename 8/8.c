#include <limits.h>
#include <stdio.h>

int myAtoi(char * str){
    char * s=str;
    // 2^31-1: 2147483647, -2^31: 2147483648
    int preNumber  = 214748364;
    int lastNumber = 7;
    int flag = 1;

    while (*s == ' ') {
        s++;
    }

    if (*s == '-' || *s == '+') {
        if (*s == '-') {
            flag = -1;
            lastNumber = 8;
        }
        s++;
    }

    int number = 0;
    while (*s) {
        if (*s < '0' || *s > '9' ) {
            break;
        }

        int cur = *s - '0';
        if ( (number > preNumber) || (number == preNumber && cur >= lastNumber) ) {
            return flag > 0 ? INT_MAX: INT_MIN;
        }
        number = number * 10 + cur;

        s++;
    }

    return flag > 0 ? number : -number;
}

int main()
{
    char s[] = "-91283472332";
    int r = myAtoi(s);
    printf("%d\n", r);
    return 0;
}