// Add or Exists queries - May 10
function solution(queries: string[][]): string[] {
    let solution: string[] = [];
    let count: string[] = [];
    for (let i = 0; i < queries.length; i++) {
        if (queries[i][0] === "ADD") {
            count.push(queries[i][1])
            solution.push("")
        } 
        else if (queries[i][0] === "REMOVE") {
            let g;
            if (count.includes(queries[i][1])) {
                g = count.indexOf(queries[i][1]);
                count.splice(g, 1)
                solution.push("true")
            } else {
                solution.push("false")
            }
        }
        else if (queries[i][0] === "EXISTS") {
            if (count.includes(queries[i][1])) {
                solution.push("true")
            } else {
                solution.push("false")
            }
        } 
        else if (queries[i][0] === "GET_NEXT") {
            let greaterNumbers: number[] = [];
            // Turn count array into number array so we can sort
            const parsedCount = count.map( number => {
                return parseInt(number);
            })
            
            // If number in count is greater than input value, add it to new array
            for(let j = 0; j < parsedCount.length; j++) {
                if (parsedCount[j] > parseInt(queries[i][1])) {
                    greaterNumbers.push(parsedCount[j]);
                }
            }
            
            if (greaterNumbers.length !== 0) {
                greaterNumbers.sort((a, b) => a - b);
                solution.push(greaterNumbers[0].toString())
            } else {
                solution.push("")
            }
        } 
    }
    return solution;
}

// Example queries and output:
/*
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "2"],
    ["ADD", "4"],
    ["GET_NEXT", "1"],
    ["GET_NEXT", "2"],
    ["GET_NEXT", "3"],
    ["GET_NEXT", "4"],
    ["REMOVE", "2"],
    ["GET_NEXT", "1"],
    ["GET_NEXT", "2"],
    ["GET_NEXT", "3"],
    ["GET_NEXT", "4"]
]

solution(queries) = ["", "", "", "", "2", "4", "4", "", "true", "2", "4", "4", ""]
*/
