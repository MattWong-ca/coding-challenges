//242. Valid Anagram - Leetcode Easy

public class Solution {
    public bool IsAnagram(string s, string t) {
        
        char[] sArray = s.ToCharArray();
        char[] tArray = t.ToCharArray();
        
        Array.Sort(sArray);
        Array.Sort(tArray);
        
        string sString = new String(sArray);
        string tString = new String(tArray);

        if ( String.Equals(sString, tString) ) {
            return true;
        } else {
            return false;
        }
    }
}
