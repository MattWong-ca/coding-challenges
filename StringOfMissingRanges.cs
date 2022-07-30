using System;
using System.Linq;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        int[] array1 = new int[] { 0, 1, 5, 7, 100 };
        int maxValue = 100;
        Console.WriteLine(missingRanges(maxValue, array1));
    }
    
    public static string missingRanges(int maxValue, int[] arrayValues) {
        string concatenatedRanges = null;
		
		// Case where array is empty.
		if ( arrayValues.Length == 0 ) { return "0-" + (maxValue - 1).ToString(); }
		
		// Case where array has single value of 0.
		if ( arrayValues.Length == 1 && arrayValues[0] == 0 ) { return "1-" + (maxValue - 1).ToString(); }
		
		// Cases where array start with 0; the zero is removed. 
		if ( arrayValues[0] == 0 ) { arrayValues = arrayValues.Skip(1).ToArray(); }
		
	    for ( int i = 0; i < arrayValues.Length - 1; i++ ) {
			string range = returnRange(arrayValues[i], arrayValues[i+1]);
				
			if ( i == 0 ) {
				concatenatedRanges = concatenatedRanges + range;
			} 
			else if ( range != "" ) {
				concatenatedRanges = concatenatedRanges + "," + range;
			}

			}
		
			if ( arrayValues.Last() != maxValue ) {
				concatenatedRanges = concatenatedRanges + "," + returnRange(arrayValues.Last(), maxValue);
			}

			if ( concatenatedRanges.Substring(0, 1) == "," ) {
				concatenatedRanges = concatenatedRanges.Substring(1);
			}

			return concatenatedRanges;
    }
    
	// Helper function that returns a range for one specific iteration. 
    public static string returnRange(int one, int two) {
        if ( two - one == 2 ) {
            return (one + 1).ToString();
	    } else if ( two - one == 1) {
			return "";
		} else {
            string lowerBound = (one + 1).ToString();
            string upperBound = (two - 1).ToString(); 
            return lowerBound + "-" + upperBound;
	    }

    }
}
