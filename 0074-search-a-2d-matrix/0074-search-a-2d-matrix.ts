function searchMatrix(matrix: number[][], target: number): boolean {
        // ROWS = len of matrix
        const ROWS: number = matrix.length;
        // COLS = len of matrix[0]
        const COLS: number = matrix[0].length;
        
                
        // init top = 0
        let top: number = 0;
        
        // init bottom = ROWS - 1
        let bot: number = ROWS -1;
        
        // while top <= bottom:
            // middle = (top + bot) // 2
            // if target > matrix[middle][-1] - greatest value in the row:
                // top = middle + 1
            // else if target < matrix[row][0] - smallest value in the row:
                // bottom = middle - 1
            // else:
                // break
        while (top <= bot) {
            const mid = Math.floor((top + bot) / 2);
            if (target > matrix[mid][COLS - 1]) {
                top = mid + 1;
            } else if (target < matrix[mid][0]) {
                bot = mid - 1;
            } else {
                break;
            }
        }  

        // if top > bottom:
        //    return False
        if (top > bot) return false;
        
        // row = (top + bottom) // 2
        // l, r = 0, COLS - 1
        let row: number = Math.floor((top + bot) / 2);
        let left: number = 0;
        let right: number = COLS - 1;
    
        // while left <= right:
            // mid = (left + right) // 2
            // if target > matrix[row][mid]:
                // left = mid + 1
            // else if target < matrix[row][mid]:
                // right = mid - 1
            // else:
                // return True
        while (left <= right) {
            let mid: number = Math.floor((left + right) / 2);
            if (target > matrix[row][mid]) {
                left = mid + 1;
            } else if (target < matrix[row][mid]) {
                right = mid - 1;
            } else {
                return true;
            }
        }   
        
        // return False
        return false;
};