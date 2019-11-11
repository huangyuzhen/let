#include <stdio.h>

int maxDivide(divisor)
{
    // 被除数 -2^31, 特例
    if (divisor == -1) return  2147483647;
    if (divisor ==  1) return -2147483648;
    if (divisor == -2147483648) return 1;

    int negFlag = divisor > 0;
    if (divisor < 0 ) divisor = -divisor;

    int number = 2147483647;
    int result = 0;
    for(int i=30; i>=0; i--) {
        int k = number >> i;
        if (k >= divisor) {
            result += 1 << i;
            number -= divisor << i;
        }
    }
    if (number + 1 >= divisor) result ++;

    return negFlag ? - result: result;
}

int divide(int dividend, int divisor)
{
    if (dividend == -2147483648) return maxDivide(divisor);
	if (dividend == 0 ) return 0;

    if (divisor == -2147483648) return 0;
    if (divisor == 1) return dividend;

    int negFlag  = (divisor ^ dividend) < 0;
    if (divisor  < 0) divisor  = -divisor;
    if (dividend < 0) dividend = -dividend;

    int number = dividend;
    int result = 0;
    for(int i=30; i>=0; i--) {
        int k = number >> i;
        if (k >= divisor) {
            result += 1 << i;
            number -= divisor << i;
        }
    }

    return negFlag ? -result : result;
}

int main()
{
    // int a = -2147483647;
    int a = -2147483648;
    // int a = -10;
    int b = 3;

    int s = divide(a, b);
    printf("%d\n", s);

    return 0;
}