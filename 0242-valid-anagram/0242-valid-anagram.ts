function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }
    
    const firstStringMap : Map<string,number> = new Map();
    for (const char of s) {
        firstStringMap.set(char,(firstStringMap.get(char) || 0) + 1);
    }
    
    console.log(firstStringMap);
    
    for (const char of t) {
        if(!firstStringMap.has(char)) {
            return false;
        } else {
            firstStringMap.set(char,firstStringMap.get(char)! -1);
            
            if(firstStringMap.get(char) === 0) {
                firstStringMap.delete(char);
            }
        }
    }
    
    
    return firstStringMap.size === 0;
    
};