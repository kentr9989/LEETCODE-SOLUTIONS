/**
 * @param {number[]} nums
 * @return {number[]}
 */
let productExceptSelf = (nums) => {
  //[x,y,z]
  let answerArr = [];

  //right product
  //[(1*y),(1*z),z]
  // want it to be [(1*y) * (1*z),(1*z),1]
  //left product
  //[1,(1*x),(1*y)]
  // want it to be [1,(1*x),(1*y*x)]
  let rightProduct = 1;
  let rightProductArr = [];
  for (let i = 0; i < nums.length; i++) {
    if (i + 1 < nums.length) {
      rightProductArr[i] = 1 * nums[i + 1];
    } else if (i === nums.length - 1) {
      rightProductArr[i] = 1;
    }
  }

  for (let k = rightProductArr.length - 1; k >= 0; k--) {
    if (k === rightProductArr.length - 1) {
      rightProductArr[k] = rightProductArr[k] * rightProduct;
    } else {
      rightProductArr[k] = rightProductArr[k + 1] * rightProductArr[k];
    }
  }
  // left 1st
  let leftProductArr = [];
  for (let i = nums.length - 1; i >= 0; i--) {
    if (i === 0) {
      leftProductArr[i] = 1;
    } else if (i - 1 >= 0) {
      leftProductArr[i] = 1 * nums[i - 1];
    }
  }
  // console.log(leftProductArr);
  // left 2nd
  for (let i = 0; i < nums.length; i++) {
    if (i === 0) {
      leftProductArr[i] = leftProductArr[i];
    } else {
      leftProductArr[i] = leftProductArr[i - 1] * leftProductArr[i];
    }
  }

  for (const i in nums) {
    if (leftProductArr[i] * rightProductArr[i] === -0) answerArr[i] = 0;
    else {
      answerArr[i] = leftProductArr[i] * rightProductArr[i];
    }
    // answerArr[i] = leftProductArr[i] * rightProductArr[i];
  }
  // console.log(answerArr);
  return answerArr;
};
