// Create a function called checkNumber() that takes no parameter.
function checkNumber() {

    for (let x = 0; x <= 100; x++) {
        if (x === 0) {
            console.log(x + " is even");
        } else if (x % 2 === 0) {
            console.log(x + " is even");
        } else {
            console.log(x + " is odd");
        }
    }
}
    //Call the function
    checkNumber()
