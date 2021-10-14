function hotelCost(){
    let nights = parseInt(prompt("How many nights are you staying in the hotel? "))
    let totalCost = nights *= 140;
    if (isNaN(nights)) {
        nights= parseInt(prompt("You did not enter a number, Please enter a number."))
        totalCost = nights *= 140;
    }
    return(alert(`The total cost of your hotel is ${totalCost}`))
}


function planeRideCost() {
    let destinationUser = prompt("where would you like to travel ?")
    //     If the user doesn’t answer or if the answer is not a string, ask again.
    if(typeof destinationUser!=="string" || destinationUser==="") {
        destinationUser = prompt("where would you like to travel ?")
    }

    // London”: 183$
    if(destinationUser==="London") {
        var TotalPlaneRideCost = 183
    }
    // “Paris” : 220$
    else if(destinationUser==="Paris") {
        TotalPlaneRideCost = 220
    }
    //     All other destination : 300$
    else {
        TotalPlaneRideCost = 300
    }
    return TotalPlaneRideCost
}


function rentalCarCost() {
    // It should ask the user for the number of days they would like to rent the car.
    let numberDayUser = prompt("How many days do you want to rent your car ?")
    //     If the user doesn’t answer or if the answer is not a number, ask again.
    if(typeof numberDayUser!="number"||numberDayUser==="") {
        numberDayUser = prompt("How many days do you want to rent your car ?")
    }
    //     Calculate the cost to rent the car. The car costs $40 everyday.
    let totalRentCarCosts = numberDayUser * 40
    //     If the user rents a car for more than 10 days, they get a 5% discount.
    if(numberDayUser>10) {
        totalRentCarCosts = (numberDayUser/10)*2
    }
    // The function should return the total price of the car rental.
    return totalRentCarCosts

}

function totalVacationCost() {
    hotelCost()
    planeRideCost()
    rentalCarCost()
}

