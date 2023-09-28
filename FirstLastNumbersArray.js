// Array Question - turn array sequence into first/last until middle is reached

function newArray(numbers) {
// 5 2 3 1 9 8 1
// 5 8 2 9 3 1
// have 2 lines of code that add into the array
// one of them pushes from front
// other pushes from the end
// for loop
const newNumbers = [];
for ( let i = 0; i < numbers.length/2; i++ ) {
newNumbers.push(numbers[i]);
if ( i !== numbers.length - 1 - i ) {
newNumbers.push(numbers[numbers.length - 1 - i]);
}
}
return newNumbers;
}
