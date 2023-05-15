import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
       Map<Integer,Integer> checkDuplicate = new HashMap<>();
       for(int num : nums) {
           if(checkDuplicate.get(num) == null) {
               checkDuplicate.put(num,1);
           } else {
               int value = checkDuplicate.get(num);
               checkDuplicate.replace(num,value + 1);
               return true;
           }
       }
       return false;
    }
}

