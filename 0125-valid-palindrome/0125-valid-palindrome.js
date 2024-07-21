/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // Write a function to check if character is alphanumeric
    // It is if character is between 'a' and 'z'
    // OR character is between 'A' and 'Z'
    // OR character is between '0' and '9'
    function isAlphanumeric(char) {
        return ( char >= 'a' && char <= 'z') ||
               ( char >= 'A' && char <= 'Z') ||
               ( char >= '0' && char <= '9');
    }
    // Init left and right
    let left = 0;
    let right = s.length - 1;
    
    // while left < right
    // while left < right && s[left] is not alphanumeric
    // then left++;
    // while left < right && s[right] is not alphanumeric
    // right--
    // if s[left] !== s[right]
    // return false
    // then left++ and right--
    while(left < right) {
        while(left < right && !isAlphanumeric(s[left])) {
            left++;
        }
        while(left < right && !isAlphanumeric(s[right])) {
            right--;
        }
        if(s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }
        left++;
        right--;
    }
    
    // when escape loop then return true;
    return true;
    
};