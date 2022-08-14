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

// Suppose Big-O was asked and a better runtime was desired. 
// Another option would be to use binary search
int countPrefixes(String prefix) {
	int count = 0;
    int leftElement = 0;
	int rightElement = dictionary.Length;
		
	while (leftElement < rightElement) {
	    string middleWordSubstring = dictionary[(leftElement + rightElement) / 2].substring(0, prefix.Length);

	    if ( middleWordSubstring == prefix ) {
	        leftElement = (leftElement + rightElement) / 2; //??
	    }

		if ( middleWordSubstring.compareTo(prefix) == -1 ) {
			leftElement = (leftElement + rightElement) / 2;
		} 
		else if ( middleWordSubstring.compareTo(prefix) == 1 ) {
			rightElement = (leftElement + rightElement) / 2;
		} 
		else {
	        rightElement = (leftElement + rightElement) / 2;
		}
    }
}
