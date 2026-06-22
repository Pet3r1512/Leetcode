function missingNumber(nums: number[]): number {
    const n = nums.length;
    const sumFrom0ToN = n*(n + 1)/2
    const sumOfNums = nums.reduce((sum, p) => sum + p)

    return sumFrom0ToN - sumOfNums
}

console.log(missingNumber([3,0,1]))
console.log(missingNumber([0,1]))
console.log(missingNumber([9,6,4,2,3,5,7,0,1]))