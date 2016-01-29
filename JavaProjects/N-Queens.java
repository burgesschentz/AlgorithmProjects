// QESTION: LEETCODE
// PROGRAM AUTHOR: TIANZHI CHEN

// The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
//
// Given an integer n, return all distinct solutions to the n-queens puzzle.
//
// Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
//
// For example,
// There exist two distinct solutions to the 4-queens puzzle:
//
// [
//  [".Q..",  // Solution 1
//   "...Q",
//   "Q...",
//   "..Q."],
//
//  ["..Q.",  // Solution 2
//   "Q...",
//   "...Q",
//   ".Q.."]
// ]

public class Solution {
	ArrayList<List<String>> rt;
    public List<List<String>> solveNQueens(int n) {
    	rt = new ArrayList<List<String>>();
    	StringBuilder sb = new StringBuilder();
    	for(int i = 0; i < n; i++){
    		sb.append('.');
    	}
    	String row = sb.toString();
    	List<String> board = new ArrayList<String>();
    	for(int i = 0; i < n; i++){
    		board.add(row);
    	}
    	for(int i = 0; i < n; i++){
    		helperQ(board, 0,i);
    	}
    	return rt;
    }
    public void helperQ(List<String> board, int row, int column){
    		if(isLegalQueen(board, row, column)){

    			String r = board.get(row);
    			board.set(row, r.substring(0, column) + 'Q' + r.substring(column+1));
    			if(row == board.size() - 1){
    				rt.add(new ArrayList<String>(board));
    			}
    			for(int i = 0 ; i < board.size(); i++){
    				helperQ(board, row+1,i);
    			}
    			board.set(row, r.substring(0, column) + '.' + r.substring(column+1));
    		}
    	}
	public boolean isLegalQueen(List<String> board, int row, int column){

		int offset = 1;
		for(int i = row - 1; i >= 0 ; i --){
			if((column + offset < board.get(0).length() && board.get(i).charAt(column + offset) == 'Q') ||
					(column - offset >= 0 && board.get(i).charAt(column - offset) == 'Q') ||
					(board.get(i).charAt(column) == 'Q' )){
					return false;
			}else{
				// legal
			}
			offset ++;
		}
		return true;
	}
}
