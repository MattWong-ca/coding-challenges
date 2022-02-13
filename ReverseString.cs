using System;
using static System.Console;

class Program {
    public static void Main (string[] args) {
        Write("Enter a word: ");
        string userInput = ReadLine();

        //turns user's word into array of characters
        char[] stringtoArray = userInput.ToCharArray();

        //for loop outputs characters in array from last to first
        for ( int i = userInput.Length - 1; i > -1; i-- ) {
            Write(stringtoArray[i]);
        }

        WriteLine();
    }
}
