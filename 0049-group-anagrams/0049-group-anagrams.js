/**
 * @param {string[]} strs
 * @return {string[][]}
 */
let groupAnagrams = (strs) => {
  let newArr = {};
  let resArr = [];
  for (const str of strs) {
    splitStr = str.split("");

    sortSplitStr = splitStr.sort().join();

    if (newArr[sortSplitStr] === undefined) {
      newArr[sortSplitStr] = [str];
      // newArr.sortSplitStr.push(str);
    } else {
      newArr[sortSplitStr].push(str);
    }
  }
  // console.log(newArr);
  Object.entries(newArr).forEach(([key, value]) => {
    let subNewArr = [];
    value.forEach((v) => subNewArr.push(v));
    resArr.push(subNewArr);
  });
  return resArr;
  // console.log(resArr);
};