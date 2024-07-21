/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // Init map to store character : index
    // Init maxLength equal 0 
    // Init left to be 0 
    let map = new Map();
    let maxLength = 0;
    let left = 0;
    
    // For (right = 0 ; right < s.length ; right++)
    //     EXP: We remove all character from the map
    //     and move left up to avoid duplicate characters 
    //     and delete all character before the duplicate characters 
    //     while map has s[right]:
    //         delete s[left] from map
    //         increase the position of left
    //     set the position of element s[right] and its index
    //     Assign maxLength by compare maxLength with right - left + 1
    for (let right = 0; right < s.length; right++) {
        while(map.has(s[right])) {
            map.delete(s[left]);
            left++;
        }
        map.set(s[right],right);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    // return maxLength
    return maxLength;
};