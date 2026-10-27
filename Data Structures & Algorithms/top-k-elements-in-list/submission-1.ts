class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const myMap = new Map<number,number>();
        for(let i=0;i<nums.length;i++){
            myMap.set(Number(nums[i]), (myMap.get(nums[i]) ?? 0) + 1);
        }
        const highestFirstMap = new Map(
    [...myMap.entries()].sort((a, b) => Number(b[1]) - Number(a[1]))
);
        
        const numericKeys = Array.from(highestFirstMap.keys()).slice(0, k);
        return numericKeys;
    }
    
}
