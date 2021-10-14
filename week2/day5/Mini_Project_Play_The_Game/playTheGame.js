function playTheGame() {
    //In the function, start by asking the user
    let playUser = confirm("Would you like to play ?")
    // If the answer is false, alert “No problem, Goodbye”.
    if(playUser==false) {
        alert("No problem, Goodbye")
    }
    // If his answer is true, follow these steps:
    else {

        let userNumber = parseInt(prompt("Enter a number between 0 and 10"), 10)
        while (isNaN(userNumber)) {
            userNumber = parseInt(prompt("Enter a number between 0 and 10"), 10)
        }
        if (!(userNumber > 0 && userNumber <= 10)) {
            console.log("Sorry it’s not a good number, Goodbye")


        } else if (userNumber > 0 && userNumber <= 10) {
            let computerNumber = Math.round(Math.floor(Math.random() * 11))
        }
    }

}
function test(userNumber,computerNumber) {
    if(userNumber==computerNumber) {
        alert("WINNER")
        return
    }
    if(userNumber>computerNumber) {
        alert("Your number is bigger then the computer’s, guess again")

        let userNumber = parseInt(prompt("Enter a number between 0 and 10"), 10)
        while (isNaN(userNumber)) {
            userNumber = parseInt(prompt("Enter a number between 0 and 10"), 10)
        }
    }
    if(userNumber>computerNumber) {
        alert("Your number is smaller then the computer’s, guess again")

        let userNumber = parseInt(prompt("Enter a number between 0 and 10"), 10)
        while (isNaN(userNumber)) {
            userNumber = parseInt(prompt("Enter a number between 0 and 10"), 10)
        }
    }
    if (userNumber == 3)
    {
        alert("out of chances");
    }
}
