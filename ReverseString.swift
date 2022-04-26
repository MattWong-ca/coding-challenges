//344. Reverse String - Leetcode Easy

class Solution {
    func reverseString(_ s: inout [Character]) {
        s.reverse()
        for char in s {
            print(char)
        }
    }
}
