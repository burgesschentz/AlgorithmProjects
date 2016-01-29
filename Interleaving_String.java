// QESTION: LEETCODE
// PROGRAM AUTHOR: TIANZHI CHEN

// Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
//
// For example,
// Given:
// s1 = "aabcc",
// s2 = "dbbca",
//
// When s3 = "aadbbcbcac", return true.
// When s3 = "aadbbbaccc", return false.

public class Solution {
    int[][] dp;
    public boolean isInterleave(String s1, String s2, String s3) {
        dp = new int[s1.length()+1][s2.length()+1];
        return isInterleaveRec(s1,s2,s3,dp);
    }
    public boolean isInterleaveRec(String s1, String s2, String s3, int[][] dp) {
        if(dp[s1.length()][s2.length()] != 0){
            return false;
        }

        if(s1.equals("") && s2.equals("") && s3.equals("")){
            return true;
        }else if(s1.equals("")){
            return s2.equals(s3);
        }else if(s2.equals("")){
            return s1.equals(s3);
        }else if(s3.equals("")){
            dp[s1.length()][s2.length()] = 1;
            return false;
        }else if(s1.length() + s2.length() != s3.length()){
            dp[s1.length()][s2.length()] = 1;
            return false;
        }
        if(s1.charAt(0) == s3.charAt(0) && isInterleaveRec(s1.substring(1), s2, s3.substring(1),dp)){
            return true;
        }

        if(s2.charAt(0) == s3.charAt(0) && isInterleaveRec(s1, s2.substring(1), s3.substring(1),dp)){
            return true;

        }else{
            dp[s1.length()][s2.length()] = 1;
            return false;
        }

    }


}
