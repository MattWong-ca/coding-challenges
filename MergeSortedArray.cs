// 88. Merge Sorted Array - Leetcode Easy

public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        // Goes through 2nd half of nums1 to add new #'s to array
        for ( int i = m; i < nums1.Length; ) {
            // Goes through nums2 to add these values into nums2
            for ( int j = 0; j < nums2.Length; j++ ) {
                nums1[i] = nums2[j];
                // Needs to be placed here so that nums1[i] 
                // is incremented each time j is incremented
                i++;
            }
        }
        Array.Sort(nums1);
    }
}


// Other solution that works - how can you improve n^2 runtime above?
// int j =0;
// for(int i=m;i<nums1.Length;i++)
// {
// nums1[i] = nums2[j];
// j++;                
// }
// Array.Sort(nums1);


// Why didn't this work?
// if ( nums1.Length != m ) {
//     nums1 = nums1.Take(m).ToArray();
// }
// nums1.Concat(nums2).ToArray();
// Array.Sort(nums1);
