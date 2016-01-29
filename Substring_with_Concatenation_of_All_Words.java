// QESTION: LEETCODE
// PROGRAM AUTHOR: TIANZHI CHEN

// You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
//
// For example, given:
// s: "barfoothefoobarman"
// words: ["foo", "bar"]
//
// You should return the indices: [0,9].
// (order does not matter).

public class Solution {

    public static List<Integer> findSubstring(String s, String[] words) {

    	List<Integer>  rt = new LinkedList<Integer>();

    	HashMap<String, Integer> requiredWords = new HashMap<String, Integer>();
    	HashMap<String, Integer> sWords = new HashMap<String, Integer>();
    	int numWords = words.length;
    	int wordLength = words[0].length();
    	for( String word : words){
    		requiredWords.put(word, requiredWords.getOrDefault(word, 0) + 1);
    	}
    	for(int start = 0; start < wordLength; start++){
    		sWords = new HashMap<String, Integer>();
    		int begin = start;
    		int wordCount = 0;
    		for(int j = start; j <= s.length() - wordLength; j += wordLength){
        		String str = s.substring(j, j + wordLength);
        		if(requiredWords.getOrDefault(str, 0) != 0){
        			wordCount ++;
        			sWords.put(str, sWords.getOrDefault(str, 0) + 1);
        			while(sWords.getOrDefault(str, 0) > requiredWords.getOrDefault(str, 0)){//getOrDefault: just to be safe, leave it for now

        				String kickOut = s.substring(begin, begin + wordLength);
        				begin += wordLength;
        				sWords.put(kickOut, sWords.getOrDefault(kickOut, 0) - 1);
        				wordCount --;
        			}
        			if(numWords == wordCount){
        				rt.add(begin);
        			}
        		}else{
        			begin = j + wordLength;
        			wordCount = 0;
        			sWords = new HashMap<String, Integer>();
        		}
    		}
    	}
    	return rt;
    }
}
