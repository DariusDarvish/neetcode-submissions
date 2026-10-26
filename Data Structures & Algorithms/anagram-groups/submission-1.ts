class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const myMap = new Map();
        for(let i=0;i<strs.length;i++){
            const sortedText = strs[i].split('').sort().join('');
            // If the key doesn't exist, initialize it with an empty array
            myMap.set(sortedText, myMap.get(sortedText) ?? []); 
  
            // Push the new item into the array
            myMap.get(sortedText).push(strs[i]);
            }
        return [...myMap.values()];
    }
}
