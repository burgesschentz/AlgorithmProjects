//  QESTION: LEETCODE
//  PROGRAM AUTHOR: TIANZHI CHEN
// Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

// Return all such possible sentences.
//
// For example, given
// s = "catsanddog",
// dict = ["cat", "cats", "and", "sand", "dog"].
//
// A solution is ["cats and dog", "cat sand dog"].

public class Solution {

    public List<String> wordBreak(String s, Set<String> wordDict) {

        List<String>[] hm = new List<String>[s.length() + 1];
    	return wordBreakRec(s,wordDict, hm);
    }
	public List<String> wordBreakRec(String s, Set<String> wordDict, List<String>[] hm) {

	    if(hm[s.length()] != null ){
	        return hm[s.length()];
	    }
	    if(s.length() == 0){
	    	return null;
	    }
	    LinkedList<String> sentences = new LinkedList<String>();
    	for(String word : wordDict){
    		if(s.startsWith(word)){
    			List<String> returnedSentences = wordBreakRec(s.substring(word.length()), wordDict, hm);
    			if(returnedSentences == null){
    				sentences.add(word);
    			}else{
    				for(String t : returnedSentences){
        			    sentences.add(word +" "+ t);
        			}
    			}
    		}
    	}
    	hm[s.length()] =  sentences;
    	return sentences;
    }
}
