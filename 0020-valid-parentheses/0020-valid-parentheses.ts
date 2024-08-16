function isValid(s: string): boolean {
        // Init stack - array in TypeScript
        const stack: string[] = [];
        // Init map of 3 pair parentheses
        const endToOpen: Map<string,string> = new Map();
        endToOpen.set(")","(");
        endToOpen.set("}","{");
        endToOpen.set("]","[");
    
        
        // Loop through for every character
        //  If character is close character:
        //      check if top of stack is correct open character:
        //          pop from the stack
        //      else:
        //          return false
        //  else:
        //      append character to the stack
        // Return true if stack is empty, otherwise false
        for (const char of s) {
            if (endToOpen.has(char)) {
                if (stack[stack.length - 1] === endToOpen.get(char)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(char);
            }
        }
    
        return stack.length === 0;
};