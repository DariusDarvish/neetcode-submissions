class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let myMap = new Map<number,number>;
        for(let i=0;i<nums.length;i++){
            const value=target-nums[i]
            if (myMap.has(value)){
                return [myMap.get(value)!, i];
            }
            myMap.set(nums[i],i)
        }
    }
}
