// class Solution {
//     public boolean containsDuplicate(int[] nums) {
//         System.out.println("hi");
//         return false;
//     }
// }

import java.util.List;
import java.util.HashSet;
class Solution {
public boolean containsDuplicate(int[] nums) {
HashSet num = new HashSet<>();
for(int i=0; i<nums.length;i++){
num.add(nums[i]);
}
if(num.size()!=nums.length)
return true;
else
return false;
}
}