let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.
people.shift()
//     Write code to replace “James” to “Jason”.
people.splice(3,1,"Jason")
// Write code to add your name to the end of the people array.
people.push("raphael")
//     Using a loop, iterate through the people array and console.log each person.
for(let i in people ) {
    console.log(people[i])
}
//     Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
for(let i in people ) {
    if (people[i]=="Jason") {break}
}
///     Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
people.splice(1,1)
//     Write code that console.logs Mary’s index. take a look at indexOf on google.
console.log(people.indexOf("Mary") )
//     Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
console.log(people.indexOf("Foo") )
// IT RETURNS -1 BECAUSE FOO IS NOT IN THE LIST
// Create a variable called last which value is the last element of the array.
let last = people[people.length-1]
//     Hint: What is the relationship between the index of the last element in the array and the length of the array?.

