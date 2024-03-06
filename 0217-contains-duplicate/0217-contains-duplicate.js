/**
 * @param {number[]} nums
 * @return {boolean}
 */
let containsDuplicate = (nums) => {
    let sortNums = nums.sort();
    let prevNum = null;
    for (const num of sortNums) {
       if (prevNum === num) {
           return true;
       }
       prevNum = num
    }
    return false;
}

// console.log(containsDuplicate([1,2,3,1]));