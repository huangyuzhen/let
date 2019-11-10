#include <stdio.h>


int divide(int dividend, int divisor)
{
    int isIntMin = 0;
    if (dividend == -2147483648) {
        if (divisor == -1) {
            return 2147483647;
        }
        isIntMin = 1;
    }
	if (dividend == 0) return 0;

    if (divisor == 1) return dividend;
    if (divisor  == -2147483648) {
        if (dividend == -2147483648) {
            return 1;
        } else {
            return 0;
        }
    }

    int negFlag  = 0;
    if (divisor < 0) {
        negFlag = !negFlag;
        divisor  = -divisor;
    }

    if (dividend < 0) {
        negFlag = !negFlag;
        if (dividend == -2147483648) {
            isIntMin = 1;
            dividend = 2147483647;
        } else {
            dividend = -dividend;
        }
    }

    int result = 0;
    for(int i=31; i>=0; i--) {
        int k = dividend >> i;
        if (k >= divisor) {
            result += 1 << i;
            dividend -= divisor << i;
        }
        if (i==0 && isIntMin) {
            if (dividend+1 >= divisor) {
                result += 1;
            }
        }
    }

    return negFlag ? -result:result;
}

int main()
{
    // int a = -2147483647;
    int a = -2147483648;
    int b = 4;

    int s = divide(a, b);
    printf("%d\n", s);

    return 0;
}