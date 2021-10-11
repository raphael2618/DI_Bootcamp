
let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.
people.splice(0,1)
//Write code to replace “James” to “Jason”.
people.splice(3,1,"Jason")
// Write code to add your name to the end of the people array.
people.push("Raphael")
console.log( people)
//Using a loop, iterate through the people array and console.log each person.
for(let i=0;i<people.length;i++) {
    console.log(people[i])
}
//Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
for(let i=0;i<people.length;i++) {
    console.log(people[i])
    break;
}
//Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
people.splice(1,1)
//Write code that console.logs Mary’s index. take a look at indexOf on google.
people.indexOf("Mary")
//Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
people.indexOf("foo")
//It returns -1 because the value "foo" does not exists in the array.

//Create a variable called last which value is the last element of the array.
let last = people[people.length-1]
console.log(last)
