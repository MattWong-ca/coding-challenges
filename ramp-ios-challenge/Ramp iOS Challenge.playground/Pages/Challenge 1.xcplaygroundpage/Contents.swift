/*
 Hello! Thank you for taking the time to complete our
 coding challenge. There are 3 challenges, each on a
 separate page. The clue derived from each page will
 provide instructions for the next challenge.

 We recommend turning "Editor > Show Rendered Markup"
 on for a classier experience.

 When you are done, please rename this playground to
 "first-last Ramp Challenge.playground" and submit it to
 ios-submissions@ramp.com.

 Good Luck!

 - The Ramp Mobile Team

 */

// = = = = = = = = = = = = = = = = = = = = = = = =

//: #### Challenge 1
//: The prompt below is encoded in a simple format.
//: Decode it to get the prompt for Challenge 2.

import Foundation

let prompt = """
R3JlYXQgam9iISAKCk5leHQgd2UndmUgaG9zdGVkIGEgSlNPTiBmaWxlIGF0IGF0IHRoaXMgdXJsOiBodHRwczovL2FwaS5qc29uYmluLmlvL3YzL2IvNjQ2YmVkMzI4ZTRhYTYyMjVlYTIyYTc5LiBZb3VyIGpvYiBpcyB0byB3cml0ZSBhIHNjcmlwdCB0bwpkb3dubG9hZCB0aGUgY29udGVudHMgb2YgdGhlIFVSTCAoaGludDogVGhlIFgtQUNDRVNTLUtFWSBpcyAkMmIkMTAkS2UxaXdpZUZPNy83cXNTS1UuR1lVLm9ZWFpNVzFFZUhyd2Q0eHg5eWxib0ppazVtc3RaazYpCnNvcnQgdGhlIGRhdGEgYnkgZWFjaCBlbGVtZW50cyAnYmFyJyBrZXkKZmlsdGVyIG91dCBlbGVtZW50cyB3aGVyZSAnYmF6JyBpcyBub3QgZGl2aXNpYmxlIGJ5IDMKY29uY2F0ZW5hdGUgZWFjaCBlbGVtZW50cyAnZm9vJyB2YWx1ZQoKRG8gZWFjaCBvZiB0aGVzZSBzdGVwcyB0byByZXZlYWwgdGhlIGluc3RydWN0aW9ucyBmb3IgdGhlIGZpbmFsIHBhcnQuIFJlbWVtYmVyIHRvIHNob3cgeW91ciB3b3JrIQ==
"""

// Show your work here! When you are done move on to Challenge 2
let encodingOptions: [String.Encoding] = [.utf8, .utf16, .utf32, .ascii, .isoLatin1]

for encoding in encodingOptions {
    if let data = Data(base64Encoded: prompt),
       let decodedString = String(data: data, encoding: encoding) {
        print("Decoding with \(encoding):")
        print(decodedString)
        print("")
        print("")
        print("-----")
    } else {
        print("Error decoding with \(encoding).")
    }
}
//: [Challenge 2](@next)
/*
 Great job!

 Next we've hosted a JSON file at at this url: https://api.jsonbin.io/v3/b/646bed328e4aa6225ea22a79. Your job is to write a script to
 download the contents of the URL (hint: The X-ACCESS-KEY is $2b$10$Ke1iwieFO7/7qsSKU.GYU.oYXZMW1EeHrwd4xx9ylboJik5mstZk6)
 sort the data by each elements 'bar' key
 filter out elements where 'baz' is not divisible by 3
 concatenate each elements 'foo' value

 Do each of these steps to reveal the instructions for the final part. Remember to show your work!
 */

