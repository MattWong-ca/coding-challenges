// Given an array of integers which is initially increasing and then decreasing, 
// find the INDEX of the maximum value in the array. Similar to: 
// https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/

// CLARIFYING QUESTIONS
// - What if int array is empty?
// - What if there are negative values?
// - What if it's only a single value?
// - How to turn from O(n) to O(log(n))?
int MaxValueIndex( int[] intArray ) {

	if ( intArray.Length == 0 ) { return -1; }
	
	int index = 0;
  int maxValue = intArray[0];

	for ( int i = 1; i < intArray.Length; i++ ) {
		if ( intArray[i] > maxValue ) {
			maxValue = intArray[i];
			index = i;
		}
	}
	
	return index;

}
