class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        const cleanString = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
        function checkPalindrome(s:string){
            if(0>=s.length-1){
                return true
            }
            if(s[0]==s[s.length - 1]){
                return checkPalindrome(s.slice(1,-1))
            }
            return false
        }
        return checkPalindrome(cleanString)
    }
}
