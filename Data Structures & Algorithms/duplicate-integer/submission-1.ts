class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const mySet = new Set();
        let final=false
        nums.forEach((num) => {
            console.log(mySet.has(num))
            if (mySet.has(num)){
                final=true
            }
            mySet.add(num)
        })
        return final
    }
}
