/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // Init stack
    let stack = [];
    
    // Init matching bracket object
    // key is the closing bracket
    // value is the opening bracket
    let matchingBrackets = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    // Loop through each character in s
    //   If it is a closing bracket
    //      Pop the top element
    //      If the top element doesnt match with the value of matching bracket
    //          return false
    //   else 
    //      It means it an opening bracket
    //      push the element in the stack
    for(const char of s) {
        if(matchingBrackets[char]) {
            let topElement = stack.length ? stack.pop() : '#';
            if (topElement !== matchingBrackets[char]) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }
    
    // return stack.length === 0 mean to check whether
    // there are elements left in the stack
    return stack.length === 0;
};