// QESTION: LEETCODE
// PROGRAM AUTHOR: TIANZHI CHEN
// There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
//
// For example,
// Given the following words in dictionary,
//
// [
//   "wrt",
//   "wrf",
//   "er",
//   "ett",
//   "rftt"
// ]
// The correct order is: "wertf".
//
// Note:
// You may assume all letters are in lowercase.
// If the order is invalid, return an empty string.
// There may be multiple valid order of letters, return any one of them is fine.


public class Solution {
    public String alienOrder(String[] words) {
        ArrayList<String> wz = new ArrayList<String>();
        HashMap<Character, Set<Character>> hm = new HashMap<Character, Set<Character>>();

        for(String word : words){
            wz.add(word);
        }
        alienOrderRec(wz,hm);// build the hashmap, higher -> a set of lower
        int[] count = new int[26];

        for(char c : hm.keySet()){
            for(char c0: hm.get(c)){
                count[c0 - 'a'] += 1;
            }
        }
        // so we know how many nodes point to the char

        List<Character> rt = new ArrayList<Character>();
        Queue<Character> q = new LinkedList<Character>();

        // chars in the queue has the potential to have no nodes that point to them;
        for(char c : hm.keySet()){
        	if(count[c - 'a'] == 0){
        		q.add(c);
        	}
        }

        // boolean[] outputed = new boolean[26];
        while(!q.isEmpty()){
        	char c = q.poll();
            if(count[c - 'a'] == 0){
            // 	if(outputed[c - 'a']){return "";} // no need to check here, due to this particular question
                rt.add(c);// it is bigger than every one else
                // outputed[c - 'a'] = true;
                if(!hm.containsKey(c)){
                	//do nothing
                	//means c points to nothing, we do not know what is lower than c.
                }else{
                	for(char c0: hm.get(c)){
                        count[c0 - 'a']--;
                        q.add(c0);
                    }
                }
                hm.remove(c);
            }
        }
        if(hm.keySet().size()!=0){
        	return "";
        }
        String str = "";

        for(char c : rt ){
            str += c;
        }
        return str;

    }
        public void alienOrderRec(List<String> words, HashMap<Character, Set<Character>> hm) {

        List<Character> orderedChar = new LinkedList<Character>();
        HashMap<Character, List<String>> nextLevel = new HashMap<Character, List<String>>();

        for(String word: words){
            List<String> nextLevelWords = new LinkedList<String>();
            char c = word.charAt(0);

            if(orderedChar.size() == 0 || orderedChar.get(orderedChar.size() - 1) != c){
                orderedChar.add(c);
            }

            if(word.length() != 1){
                if(!nextLevel.containsKey(c)){
                nextLevel.put(c, new LinkedList<String>());
                }
                nextLevel.get(c).add(word.substring(1));
            }

        }
        if(orderedChar.size() == 1){
        	if(!hm.containsKey(orderedChar.get(0))){
                hm.put(orderedChar.get(0), new HashSet<Character>());
            }
        }

        for(int i = 1; i < orderedChar.size(); i++){
            char c = orderedChar.get(i-1);
            if(!hm.containsKey(c)){
                hm.put(c, new HashSet<Character>());
            }
            hm.get(c).add(orderedChar.get(i));
        }


        for(List<String> lst: nextLevel.values()){
            alienOrderRec(lst, hm);
        }
    }
}
