// 49. Group Anagrams - Leetcode Medium

function groupAnagrams(strs: string[]): string[][] {

    const dictionary: { [key: string]: string[] } = {};
    const finalArray: string[][] = [];

    for (let i = 0; i < strs.length; i++) {
        let keyValue: string = strs[i].split('').sort().join('');

        if (keyValue in dictionary) {
            dictionary[keyValue].push(strs[i]);
        } else {
            dictionary[keyValue] = [strs[i]];
        }
    }

    for (const key in dictionary) {
        if (dictionary.hasOwnProperty(key)) {
            finalArray.push(dictionary[key]);
        }
    }

    return finalArray;

};
