/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    // Create a hashmap that count frequency for each num
    let mapCount = new Map();
    
    // Create a frequency 2D array (bucket sort) 
    // start from 0 to nums.length as it store the frequency
    // it contains an array of element with same frequency
    let freqCount = new Array(nums.length+1).fill().map(() => []);
    
    // Count the frequency for each element
    for(const num of nums) {
        mapCount.set(num, (mapCount.get(num) || 0 ) +1)
    }
    // console.log(mapCount);
    // Add count for frequency array
    for(const [num, freq] of mapCount) {
        freqCount[freq].push(num);
    }
    // console.log(freqCount);
    
    // Create result array
    // Loop start from freq.length - 1 to >= 0 and res.length !== k
    // Then loop for each freq[i] add res
    let res = [];
    for(let i = freqCount.length -1; i >= 0 && res.length < k; i--) {
        for(let freq of freqCount[i]) {
            if(res.length >= k) {
                return res;
            }
            res.push(freq);
        }
    }
    
    // return result array
    return res;
    
    // Time complexity and space complexity : O(n)
};