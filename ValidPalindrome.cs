//125. Valid Palindrome - Leetcode Easy

using System.Text.RegularExpressions;

public class Solution {
    public bool IsPalindrome(string s) {
        s = Regex.Replace(s, "[^a-zA-Z0-9]", String.Empty);
        s = s.ToLower();
        
        char[] charArray = s.ToCharArray();
        Array.Reverse( charArray );
        string reversed = new String( charArray );
        
        if ( s == reversed ) {
            return true;
        } else {
            return false;
        }
    }
}
