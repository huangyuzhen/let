#include <stdio.h>
#include <limits.h>

int main()
{
    // int a = 1;
    // while(a > 0) {
    //     a++;
    // }
    // printf("%d\n", a);
    // printf("%d\n", a-1);

    int b = INT_MAX;
    int i = 0;
    for(i=31; i>0; i--) {
        int c = b>>i;
        printf("%d -> %d, %02X -> %02x\n", b, c, b,c);
    }

    return 0;
}