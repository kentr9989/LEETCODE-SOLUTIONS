function containsDuplicate(nums: number[]): boolean {
    const numMap : Map<number,number> = new Map();
    
    for (const num of nums) {
        if (numMap.has(num)) {
            return true;
        }
        numMap.set(num,1);
    }
    return false;
};