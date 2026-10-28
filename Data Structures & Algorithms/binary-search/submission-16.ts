class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let left=0
        let right=nums.length-1
        while(left<=right){
            const midpoint=Math.floor((left+right)/2)
            console.log(midpoint,nums[midpoint])
            if(nums[midpoint]==target){
                return midpoint
            }
            else if(nums[midpoint]<target){
                left+=1
            }
            else{
                right-=1
            }

        }
        return -1
    }
}
