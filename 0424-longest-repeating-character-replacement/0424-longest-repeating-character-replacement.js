/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    // Init countMap to store character : its occurence
    // Init left equal 0
    // Init res equal 0
    let countMap = new Map();
    let left = 0;
    let res = 0;
    let maxF = 0;
    
    // Exp: Here we will make a sliding window
    // with left and right = 0. If the current
    // length of window - maximum occurence of character
    // is greater than k , then we delete the occurence 
    // of left character from hashmap and increase left pointer
    for(let right = 0; right < s.length; right++) {
        
        countMap.set(s[right], (countMap.get(s[right]) || 0) + 1);
        maxF = Math.max(maxF,countMap.get(s[right]))
        while( (right - left + 1) - maxF > k ) {
            countMap.set(s[left], countMap.get(s[left]) - 1);
            if(countMap.get(s[left]) === 0) {
                countMap.delete(s[left]);
            }
            left++;
        }
        
        res = Math.max(res, right-left+1);
        
    }
    
    // return res
    return res;
    
    // Time complexity : O(26n) because need to check max-occurence for every 26 letters
    // Space complexity : O(26) = O(1) because need to store at most 26 characters
};