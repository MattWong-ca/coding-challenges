//20. Valid Parentheses - Leetcode Easy

public class Solution {
    public bool IsValid(string s) {
        Stack<char> charStack = new Stack<char>();
        
        if ( s.Length % 2 != 0 ) {
            return false;
        }
        
        foreach ( char c in s.ToCharArray() ) {
            if ( c == '(' || c == '{' || c == '[' ) {
                charStack.Push(c);
            } else if ( c == ']' && charStack.Count() != 0 && charStack.Peek() == '[' ) {
                charStack.Pop();
            } else if ( c == '}' && charStack.Count() != 0 && charStack.Peek() == '{' ) {
                charStack.Pop();
            } else if ( c == ')' && charStack.Count() != 0 && charStack.Peek() == '(' ) {
                charStack.Pop();
            } else {
                return false;
            }
        }
        
        if ( charStack.Count() == 0 ) {
            return true;
        }
        return false;
    }
}
