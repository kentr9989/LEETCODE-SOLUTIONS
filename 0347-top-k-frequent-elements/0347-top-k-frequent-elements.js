/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
let topKFrequent = (nums, k) => {
  const frequencyMap = new Map();
  // Step 1 : count the frequency and set to map
  nums.forEach((num) =>
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1)
  );

  // Step 2 : Convert the frequency into array form
  // to use sort
  let freqArr = Array.from(frequencyMap.entries());

  // Step 3 : Sort the map by frequency - in ascending order
  freqArr.sort((a, b) => b[1] - a[1]);

  // Step 4 : Put the result into the array up to k
  let resArr = [];
  for (const freq of freqArr) {
    if ( k == 0) break;
    resArr.push(freq[0]);
    k--;
  }
  return resArr;
};