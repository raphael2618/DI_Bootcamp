
    let num1 = parseInt(prompt("Enter one number please"));
    //If the number given is less than 2 : return “boom”
    if(num1<2) {
            alert("Boom")
        }
    //If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
    else if(num1>2) {
        let numString = num1.toString()
        let lengthNumber= numString.length
        let result= " 0 ".repeat(lengthNumber)
        alert(result)
        }
    //If the number given is evenly divisible by 2, add a exclamation mark to the end.
    else if(num1%2==0) {
        let numString = num1.toString()
        let lengthNumber= numString.length
        let result= " 0 ".repeat(lengthNumber) + " " + "!"
        alert(result)
    }
    //If the number given is evenly divisible by 5, return the string in ALL CAPS.

    else if(num1 % 5 == 0) {
        let stringBoom = "boom"
        capitalBoom = stringBoom.toUpperCase()
        alert(capitalBoom)

    }
    //If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS
    // and add an exclamation mark to the end.
    else if(num1 % 5 == 0 && num1 % 2 == 0)  {
        let stringBoom = "boom"
        capitalBoom = stringBoom.toUpperCase()
        alert(capitalBoom + " " + "!")
    }
