function minWindow(s: string, t: string): string {
        // if t is an empty string:
        // return the empty string
        if (t === '') return ''

        // init map for s {character : count}
        const mapS: Map<string,number> = new Map();
        // init map for t {character : count}
        const mapT: Map<string,number> = new Map();

        // inject all values for map t
        for (const char of t) {
            mapT.set(char, 1 + (mapT.get(char) || 0));
        }
        console.log(mapT);
        // init have as equal 0
        let have: number = 0;
        // init need as the length of t
        let need: number = mapT.size;
        console.log(need);
        // init res to be start and end index
        let res: number[] = [-1,-1];
        // init res length to be infinity
        let resLen: number = Infinity;
        // init left pointer equal 0
        let left: number = 0; 

        // for right pointer (0 -> length of s):
        //   add the character of s[right] to map of s
        //   check if s[right] is in map of t AND
        //   s[right] equal to map_t[s[right]]:
        //       increase have by 1
        //   while have == need:
        //       Update the new res and resLen
        //       remove s[left] from map_s
        //       check if s[left] is in map_t[] AND
        //       map_s[s[left]] < map_t[s[left]]:
        //           decrease have by 1
        //       increase left pointer by 1
        for (let right = 0; right < s.length; right++) {
            mapS.set(s[right],(mapS.get(s[right]) || 0) + 1);
            if (mapT.has(s[right]) && mapT.get(s[right]) === mapS.get(s[right])) {
                have += 1;
            }
            while (have === need) {
                if ( (right - left + 1) < resLen ) {
                    resLen = right - left + 1;
                    res = [left,right];
                }
                mapS.set(s[left], (mapS.get(s[left]) || 0) - 1);
                if (mapT.has(s[left]) && mapS.get(s[left]) < mapT.get(s[left])) {
                    have -= 1;
                }
                left += 1;
            }
        }
        console.log(`${res[0]} ${res[1]}`);
        // res = [left,right]    
        // if resLen is still infinity:
        //     return "" - nothing is found
        // else:
        //     return the string from pos left to right + 1 (slicing)
        return resLen != Infinity ? s.slice(res[0],res[1] + 1) : ""; 
};