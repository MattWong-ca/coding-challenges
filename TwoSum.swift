//1. Two Sum - Leetcode Easy

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0...nums.count-1 {
            for j in 0...nums.count-1 {
                if target - nums[j] == nums[i] && i != j {
                    return [i,j]
                }
            }
        }
        return nums
    }
}
