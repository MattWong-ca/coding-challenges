//1768. Merge Strings Alternately - Leetcode Easy

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = min( word1.length(), word2.length() );
        //cout << n;
        
        string mergedString;
        
        for ( int i = 0; i < n; i++ ) {
            mergedString = mergedString + word1[i];
            mergedString = mergedString + word2[i];
        }
        //cout << mergedString;
        
        return mergedString + word1.substr( n ) + word2.substr( n );
    }
};
