//1528. Shuffle String - Leetcode Easy

public class Solution {
    public string RestoreString(string s, int[] indices) {
        char[] charArrayS = s.ToCharArray();
        
        for ( int i = 0; i < indices.Length; i++ ) {
            charArrayS[indices[i]] = s[i];
        }
        
        string newString = new string(charArrayS);
        
        return newString;
    }
}
