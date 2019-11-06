#include <stdio.h>

bool isPalindrome(int x){
    int y = 0;

    // 边界: 负数, 0
    if (x == 0) return 1;
    if (x < 0 || x % 10 == 0) return 0;

    // 比较一半
    while (x > y) {
        y = y * 10 + x % 10;
        x = x / 10;
    }

    return x == y || x == y / 10;
}

int main()
{
    int s = 121;
    int r = isPalindrome(s);
    printf("%d\n", r);
    return 0;
}