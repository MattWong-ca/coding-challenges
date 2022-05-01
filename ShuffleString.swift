//1528. Shuffle String - Leetcode Easy

class Solution {
    func restoreString(_ s: String, _ indices: [Int]) -> String {
        var sArray = Array(s) //turns given string into char array
        
        for i in 0..<indices.count {
            sArray[indices[i]] = Array(s)[i]
        }
        
        return String(sArray)
    }
}
