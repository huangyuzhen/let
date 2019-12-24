int singleNumber(int* nums, int numsSize){
    int ans = 0;
    for(int i=0; i<32; i++){
        int count = 0;
        for (int j=0; j<numsSize; j++) {
            if ((nums[j] >> i) & 1 ) {
                count ++;
            }
        }
        if (count % 3 != 0) {
            ans |= 1 << i;
        }
    }
    return ans;

}

int main()
{
    int nums[] = {-2,-2,1,1,-3,1,-3,-3,-4,-2};
    int numsSize = 10;

    int a = singleNumber(nums, numsSize);
    printf("%d\n", a);

    return 0;

}