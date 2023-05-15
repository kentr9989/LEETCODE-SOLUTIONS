import java.util.*;
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] row = new HashSet[9];
        Set<Character>[] column = new HashSet[9];
        Set<Character>[] box = new HashSet[9];
        
        for(int i = 0; i < 9; i++) {
            row[i] = new HashSet<>();
            column[i] = new HashSet<>();
            box[i] = new HashSet<>();
        }
        
        for(int i = 0; i < 9; i++) {
            for(int j = 0 ; j < 9 ; j++) {
                if(board[i][j] == '.') {
                    continue;
                }
                if(!row[i].add(board[i][j])) {
                    return false;
                }
                if(!column[j].add(board[i][j])) {
                    return false;
                }
                if(!box[(j / 3)* 3 + i / 3].add(board[i][j])){
					return false;
				}
            }
        }
        return true;
        
    }
}