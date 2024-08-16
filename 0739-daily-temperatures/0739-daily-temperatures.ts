function dailyTemperatures(temperatures: number[]): number[] {
        // Init res array
        const res: number[] = new Array(temperatures.length).fill(0);
        // Init stack of [temp, index]
        const stack: [number,number][] = [];
        // Iterate through the temperatures array
            // While stack is not empty and the current temperature is greater than the top of the stack:
            //      pop the top of the stack
            //      add the index difference to res
            // Append the current temperature and index to the stack
        for (const [index,temp] of temperatures.entries()) {
            while(stack.length !== 0 && temp > stack[stack.length -1][0]) {
                const [stackTemp, stackIndex] = stack.pop();
                res[stackIndex] = index - stackIndex;
            }
            stack.push([temp,index]);
        }   
      
        // Return the result array
        return res;
    
};