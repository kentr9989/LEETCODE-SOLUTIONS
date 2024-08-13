class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character,Integer> firstStringMap = new HashMap<>();
        
        for (char c: s.toCharArray()) {
            firstStringMap.put(c, firstStringMap.getOrDefault(c,0) + 1);
        }
        System.out.println(firstStringMap);
        
        for (char c : t.toCharArray()) {
            if (!firstStringMap.containsKey(c)) {
                return false;
            } 
            firstStringMap.put(c, firstStringMap.get(c) - 1);
            if (firstStringMap.get(c) == 0) {
                firstStringMap.remove(c);
            }
        }
        
        return firstStringMap.isEmpty();
    }
}