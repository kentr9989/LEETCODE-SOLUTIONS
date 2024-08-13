function groupAnagrams(strs: string[]): string[][] {
    
    // Create new map : (sortedStr,value)
    const map : Map<string,string[]> = new Map();
    
    // For each element in strs:
    //    sort the element
    //    if sort_element in map:
    //      add sort_element to the value
    //    else:
    //      add sort_element to map
    for (const element of strs) {
        let sortedStr = element.split('').sort().join('');
        if (!map.has(sortedStr)) {
            map.set(sortedStr,[]);
        } 
        map.get(sortedStr)!.push(element);
        
    }
    
    // return the values in map
    return Array.from(map.values());
    
    
    
    
    // Time complexity : O(n * klogk) where k is length for each       string
    // Space complexity: O(n*k)
};
