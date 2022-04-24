//796. Rotate String - Leetcode Easy

class Solution {
    func rotateString(_ s: String, _ goal: String) -> Bool {
        if s.count != goal.count {
            return false
        }
        
        var rotatedString = s
        
        for i in 1...s.count {
            let prefix = rotatedString.prefix(1)
            let suffix = rotatedString.suffix(rotatedString.count-1)
            
            rotatedString = "\(suffix)\(prefix)"

            //print(rotatedString)
            
            if rotatedString == goal {
                return true
            }
        }
        return false;    
    }
}
