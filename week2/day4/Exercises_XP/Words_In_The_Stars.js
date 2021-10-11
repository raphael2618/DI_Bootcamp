// Prompt the user for several words (separated by commas).
// Put the words into an array.
let items = [], action, i = 1;

while(action = prompt(`Enter words separated by a comma`)){
    items = items.concat(action.split(','));
}
console.log(items);

//     Console.log the words one per line, in a rectangular frame as seen below.
/*for(let i = 0; i < Array1.length; i++) { // external loop
    for(let j = 0; j < Array1.length; j++) { // internal loop
        if(i === 0 || i === Array1.length - 1) {
            var String1 = "*";
        }
        else {
            if(j === 0 || j === Array1.length - 1) {
                String1 += "*";
            }
            else {
                String1 += " ";
            }
        }
    }
    // newline after each row
    String1 += "\n";
}
// printing the string
console.log(String1);
*/
