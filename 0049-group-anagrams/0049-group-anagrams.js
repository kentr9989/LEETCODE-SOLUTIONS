/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // Create a new hashmap {sortedStr, [str]}
    let map = new Map();
    
    // Loop through strs
    // For each str, create sortedStr 
    // Check if sortedStr exist in map
    // If yes then push into array
    // If not then create new array
    for(let i = 0 ; i < strs.length; i++) {
        // Split to array of single character then sort and join
        let sortedStr = strs[i].split('').sort().join('');
        if(!map.has(sortedStr)) {
            map.set(sortedStr,[]);
        } 
        
        map.get(sortedStr).push(strs[i]);
        
    }
    
    // Return array from values of hashmap
    // console.log(map);
    return Array.from(map.values());
    
    // Time complexity : O(n * klogk) where k is maximum number for each       string
    // Space complexity: O(n*k)
};