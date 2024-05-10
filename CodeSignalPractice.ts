// Add or Exists queries - May 10
function solution(queries: string[][]): string[] {
    let solution: string[] = [];
    let count: string[] = [];
    for (let i = 0; i < queries.length; i++) {
        if (queries[i][0] === "ADD") {
            count.push(queries[i][1])
            solution.push("")
        } 
        else if (queries[i][0] === "EXISTS") {
            if (count.includes(queries[i][1])) {
                solution.push("true")
            } else {
                solution.push("false")
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
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]

solution(queries) = ["", "", "", "", "true", "true", "true", "false", "false", "false"]
*/
