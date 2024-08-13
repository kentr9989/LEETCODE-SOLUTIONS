class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a hashmap to store value : index
        Map<Integer,Integer> map = new HashMap<>();    
        
        // Loop through array nums
        // Find the complement through hashmap
        // If dont have then we set value : index
        // If have then return [index, complement-index]
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement),i};
            }
            map.put(nums[i],i);
        }
        
        
        // return - no solution is found
        return new int[0];
        // Time complexity : O(n)
        // Space complexity : O(n)    
    }
}