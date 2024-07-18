/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let map = new Map();
    for(const num of nums) {
        if(map.has(num)) return true;
        map.set(num,num);
    }
    return false;
};