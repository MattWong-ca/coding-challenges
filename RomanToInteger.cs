//13. Roman to Integer - Leetcode Easy

public class Solution {
    public int RomanToInt(string s) {
        
        // CLARIFY - what if string is null or empty?
        if ( s == null || s.Length == 0 ) { return 0; }
        
        // Creates dictionary of Roman numerals and their values
        Dictionary<char, int> map = new Dictionary<char, int>();
        map.Add('I', 1);
        map.Add('V', 5);
        map.Add('X', 10);
        map.Add('L', 50);
        map.Add('C', 100);
        map.Add('D', 500);
        map.Add('M', 1000);
        
        // Initializes result as value of last Roman numeral in string s
        int result = map[s[s.Length - 1]];
        
        // Iterates through string s, starting at 2nd last Roman numeral
        for ( int i = s.Length - 2; i >= 0; i-- ) {
            // If current Roman numeral is less than one after it
            // (eg. IV - 1 is less than 5)
            // result is current result minus current Roman numeral
            if ( map[s[i]] < map[s[i+1]] ) {
                result = result - map[s[i]];
            }
            // else if it's same or greater
            // (eg. II or VI)
            // it's added to current result
            else {
                result = result + map[s[i]];
            }
        }
        
        return result;
    }
}
