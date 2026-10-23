class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const mySet = new Set<number>();
        //Faster than for each
        for (const num of nums) {
            if (mySet.has(num)) {
                return true;
            }
            mySet.add(num);
        }

        return false;
    }

}
