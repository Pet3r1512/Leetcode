function arithmeticTriplets(nums: number[], diff: number): number {
    let count: number = 0
    const n: Set<number> = new Set(nums)

    for (let i = 0; i < nums.length; i++) {
        const first = nums[i]
        const second = first + diff
        const third = second + diff 

        if (n.has(second) && n.has(third)) {
            count++
        }
    }

    return count
}

console.log(arithmeticTriplets([0,1,4,6,7,10], 3))
console.log(arithmeticTriplets([4,5,6,7,8,9], 2))