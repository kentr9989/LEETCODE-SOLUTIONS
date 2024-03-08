/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
let twoSum = (nums, target) => {
  let map = {};
  let resultArr = [];

  for (const i in nums) {
    let difference = target - nums[i];
    // console.log(difference);
    map[difference] = i;
  }
//   console.log(map);

  for (const [index, value] of nums.entries()) {
    if (map[value] !== undefined && index !== parseInt(map[value])) {
      resultArr.push(index);
      resultArr.push(parseInt(map[value]));
      return resultArr;
    }
  }
  return resultArr;
};