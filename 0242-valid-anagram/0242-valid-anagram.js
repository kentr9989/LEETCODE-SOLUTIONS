/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
let isAnagram = (s,t) => {
    if(s.length !== t.length) return false;
    
    let copyS = [...s];
    repeatIndex = [];
    
    for(const letter of t) {
        index = copyS.indexOf(letter);
        if(index === -1) return false;
        copyS.splice(index,1);
    }
    return true;

}