function hotelCost() {
    // It should ask the user for the number of nights they would like to stay in the hotel.
    let nightUser = prompt("Which number of night would you like to stay ?")
    //If the user doesn’t answer or if the answer is not a number, ask again.
    if(typeof nightUser!=="number"||nightUser==="") {
        nightUser = prompt("Which number of night would you like to stay ?")
    }
    //The hotel costs $140 per night. The function should return the total price of the hotel.
    console.log(nightUser * 140 )
}

function planeRideCost() {
    let destinationUser = prompt("where would you like to travel ?")
    //     If the user doesn’t answer or if the answer is not a string, ask again.
    if(typeof destinationUser!=String || destinationUser==="") {
        destinationUser = prompt("where would you like to travel ?")
    }

    // London”: 183$
    if(destinationUser=="London") {
        var TotalPlaneRideCost = "183$"
    }
    // “Paris” : 220$
    else if(destinationUser=="Paris") {
        var TotalPlaneRideCost = "220$"
    }
    //     All other destination : 300$
    else {
        var TotalPlaneRideCost = "300$"
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
/*
function totalVacationCost() {
    hotelCost()
    planeRideCost()
    rentalCarCost()
}*/

hotelCost()
