// Given an array of integers which is initially increasing and then decreasing, 
// find the INDEX of the maximum value in the array. Similar to: 
// https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/

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
