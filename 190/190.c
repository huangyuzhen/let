uint32_t reverseBits(uint32_t n) {
    uint32_t m = 0;
    for(int i=0; i<32; i++) {
        if ((n >> i) & 1) {
            m |= (1U <<(31-i));
        }
    }
    return m;
}
