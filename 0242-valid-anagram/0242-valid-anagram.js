/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // if length s not equal t return false
    if(s.length !== t.length) {
        return false;
    }
    
    // make a hashmap to store character 
    let charCount = new Map();

    // store hashmap with char of s
    for(const char of s) {
        charCount.set(char , (charCount.get(char) || 0) + 1 );
    }
    
    // for char of t check following
    // if the hash map does not contain char return false
    // decrease the count of the hashmap
    // if the hash map contain then if count < 0 return false
    
    for(const char of t) {
        if(!charCount.has(char)) {
            return false;
        }
        charCount.set(char,charCount.get(char) - 1);
        if(charCount.get(char) < 0) {
            return false;
        }
    }
    
    return true;
    // return true because the hashmap contain both s and t
    
    // Time complexity : O(n)
    // Space complexity : O(1) because of 26 English characters
};