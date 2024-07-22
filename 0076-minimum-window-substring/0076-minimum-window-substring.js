/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    // If length of s OR length of t is empty return empty string
    if (s.length === 0 || t.length === 0) {
        return "";
    }
    
    // Init hashmap to keep count of all the unique characters in t
    // Then count all the character in t
    let mapT = new Map();
    for (const char of t) {
        mapT.set(char, (mapT.get(char) || 0) + 1);
    }
    
    // Init hashmap which keeps a count of all the unique characters in the current window
    let mapWindow = new Map();
    
    // Init Number of unique characters in t that need to be present in the desired window
    let required = mapT.size;
    
    // Init formed is used to keep track of how many unique characters in t are present in the current   window in its desired frequency 
    let formed = 0;
    
   // Init result tuple (window length, left, right)
   let res = [-1,0,0];
    
   // Init left and right pointer 
   let left = 0, right = 0;
    
   // while right < length of string s :
   //    stored character to be at pointer s[right]    
   //    Add one character from the right to the window 
   //    If the character is in mapT AND the frequency of character of window  
   //    is same as mapT: 
   //       increase formed by 1
   //    while left is less than to equal right and formed === required:
   //       store character to s[left]
   //       If res[0] === 0 OR r - l + 1 < res[0]:
   //           Update the new result tuple
   //       Set the character on windowCount to reduce by 1
   //       if mapT contains the character AND windowCount freq of character < mapT freq of character:
   //           Reduce formed by 1
   //       increase the left pointer by 1
   //    increase right pointer by 1
    
   while (right < s.length) {
       let char = s[right];
       mapWindow.set(char, (mapWindow.get(char) || 0) + 1);
       if(mapT.has(char) && mapWindow.get(char) === mapT.get(char)) {
           formed++;
       }
       
       while (left <= right && formed === required) {
           char = s[left];
           if ( res[0] === -1 || (right - left + 1) < res[0]) {
               res = [right - left + 1, left, right];
           }
           mapWindow.set(char, mapWindow.get(char) - 1);
           if(mapT.has(char) && mapWindow.get(char) < mapT.get(char)) {
               formed--;
           }
           left++;
       }
       right++;
   }
    
   //    if the result[0] === -1:
   //       return ""
   //    else
   //       return s.slice(result[1],result[2] + 1); 
   
   if (res[0] === -1) {
       return "";
   } else {
       return s.slice(res[1], res[2] + 1);
   }
    
   // Time complexity: O(m + n) where m is length of s and n is length of t
   // Space complexity: O(m + n)
};