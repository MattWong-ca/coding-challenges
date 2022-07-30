/* You are given a sorted list of distinct integers from 0 to 99, for instance [0, 1, 2, 50, 52, 75]. 
Your task is to produce a string that describes numbers missing from the list; in this case "3-49,51,53-74,76-99".

Examples:
[] “0-99”
[0] “1-99”
[3, 5] “0-2,4,6-99”

*/



using System;
using System.Linq;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        int[] array1 = new int[] { 1, 2, 3, 5, 7, 100 };
        int maxValue = 100;
        Console.WriteLine(missingRanges(maxValue, array1));
    }
    
    public static string missingRanges(int maxValue, int[] arrayValues) {
        string concatenatedRanges = null;
		
		if ( arrayValues[0] == 0 ) { arrayValues = arrayValues.Skip(1).ToArray(); } // 1, 2, 3, 5, 7, 100
		
	    for ( int i = 0; i < arrayValues.Length - 1; i++ ) {
		string range = returnRange(arrayValues[i], arrayValues[i+1]);
		Console.WriteLine("h" + range); // 1st: "" 2nd: ""
				
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
