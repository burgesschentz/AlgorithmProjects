// QESTION: LEETCODE
// PROGRAM AUTHOR: TIANZHI CHEN

// Implement regular expression matching with support for '.' and '*'.
//
// '.' Matches any single character.
// '*' Matches zero or more of the preceding element.
//
// The matching should cover the entire input string (not partial).
//
// The function prototype should be:
// bool isMatch(const char *s, const char *p)
//
// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "a*") → true
// isMatch("aa", ".*") → true
// isMatch("ab", ".*") → true
// isMatch("aab", "c*a*b") → true


public class Solution {

    public boolean isMatch(String s, String p) {
    if(p.length() == 0 && s.length() != 0){
        return false;
    }

    int[][] notMatch = new int[s.length() + 1][p.length() + 1];


    return isMatchRec(s, p, notMatch);
    }

    public boolean isMatchRec(String s, String p, int[][] notMatch) {

//        String rest;

        if(s.equals("") && p.equals("")){
            return true;
        }
        if(notMatch[notMatch.length-1 - s.length()][notMatch[0].length-1 - p.length()] == 1){
            return false;
        }


        if(p.length() >= 2 && p.charAt(1) == '*'){

            char charAnyNumOf = p.charAt(0);
            if(s.equals("")){
                return isMatchRec("", p.substring(2), notMatch);
            }

            if(isMatchRec(s, p.substring(2), notMatch)){
            	return true;
            }

            for(int i = 0; i < s.length(); i++){
                if( charAnyNumOf == '.' || s.charAt(i) == charAnyNumOf){ // if '.', loop through the whole thing

                    if(isMatchRec(s.substring(i + 1), p.substring(2), notMatch)){
                        return true;
                    }

                }else{

                    notMatch[i][notMatch[0].length-1 - p.length()+2] = 1;
                    return false;
                }
            }
            return false;

        }else{
            if(s.equals("")){
                // notMatch.add("^"+p);
                notMatch[notMatch.length-1][notMatch[0].length-1 - p.length()] = 1;
                return false;
            }else if(p.equals("")){

                notMatch[notMatch.length-1 - s.length()][notMatch[0].length-1 - p.length()] = 1;
            	return false;
            }


            char exactOne = p.charAt(0);

            if(exactOne == '.'|| s.charAt(0) == exactOne){
                return isMatchRec(s.substring(1), p.substring(1),notMatch);
            }else{
                notMatch[notMatch.length-1 - s.length() ][notMatch[0].length-1 - p.length() ] = 1;
                return false;
            }

        }
    }
}
