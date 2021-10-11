let numbers = [123, 8409, 100053, 7, 2]
// Loop through the array above and determine whether or not each number is divisible by three.
for(i in numbers) {
    if(numbers[i]%3==0) {
        console.log("The number " +  numbers[i] + " is divide by 3" )
    } else {
        console.log("The number " +  numbers[i] + " is not divide by 3")
    }

}
