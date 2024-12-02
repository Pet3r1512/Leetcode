function singleNumber(nums: number[]): number {
    let xor = 0
    let index = 0

    while (index < nums.length) {
        xor = nums[index] ^ xor
        index++
    }

    return xor
};