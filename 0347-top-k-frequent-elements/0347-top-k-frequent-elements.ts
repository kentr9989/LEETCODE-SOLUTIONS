function topKFrequent(nums: number[], k: number): number[] {
        // Create freq_map {element, count}
        const freqMap: Map<number,number> = new Map();
    
        // Put all values into the freq_map
        for (const num of nums) {
            freqMap.set(num,(freqMap.get(num) || 0) + 1);
        }
        
    
        // Init 2D freq array of length nums.length + 1
        // Each element is an array
        const freqArray: number[][] = Array.from({length: nums.length + 1}, () => []);
        
        // Put all values into the freq 2D array
        for (const [value,count] of freqMap) {
            freqArray[count].push(value);
        }
    
        // Initialize result array
        const res : number[] = [];   

        // Loop through the freq array from top to 0:
        for (let i = freqArray.length - 1; i > 0; i--) {
            for (const value of freqArray[i]) {
                res.push(value);
                if (res.length == k) {
                    return res;
                }
            }
        }   
    
        // Return result
        return res;    
};