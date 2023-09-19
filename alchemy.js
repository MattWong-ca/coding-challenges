// COUNT THE ELEMENTS - takes in array & returns an object with a count of each element in the array

function countElements(elements) {
    // Edge cases:
    // Capital letters? E
    // Empty string? ""
    // Number? 1
    let elementsDictionary = {}

    for (let i = 0; i < elements.length; i++) {
        if (elementsDictionary.hasOwnProperty(elements[i])) {
            elementsDictionary[elements[i]] += 1;
        } else {
            elementsDictionary[elements[i]] = 1;
        }
    }

    return elementsDictionary;
}

// PLAYER HAND SCORE - takes in string of face cards and returns total score of the player's hand

function playerHandScore(hand) {
    // Edge cases
    // 1. Lower case letters?
    // 2. Char other than KQJ?
    // 3. #s in string?

    let sum = 0;

    for (let i = 0; i < hand.length; i++) {
        if ( hand[i] == "K" ) {
            sum = sum + 4;
        } else if (hand[i] == "Q") {
            sum = sum + 3;
        } else {
            sum = sum + 2;
        }
    }

    return sum;
}
