// 2185. Counting Words With a Given Prefix - Leetcode Easy

public class Solution {
    public int PrefixCount(string[] words, string pref) {
        int count = 0;
        
        for (int i = 0; i < words.Length; i++) {
            // 1st time through, didn't account if pref is
            // longer than words, needed to add check
            // Eg. words --> ["leetcode","win","loops","success"]
            // Eg. pref --> "code"
			if ( words[i].Length >= pref.Length && 
                words[i].Substring(0, pref.Length) == pref ) {
				count++;
			}
		}
        
        return count;
    }
}
