let personDetailsRaphael = {fullName: "Raphael", mass: 60, height: 25};
let personDetailsDan = {fullName: "Dan", mass: 30, height: 3};


function BMI(personDetailsRaphael, personDetailsDan) {
    let massPersonDetailsR = personDetailsRaphael.mass
    let massPersonHeightR = personDetailsRaphael.height
    let BMIR = massPersonDetailsR * massPersonHeightR

    let massPersonDetailsD = personDetailsDan.mass
    let massPersonHeightD = personDetailsDan.height
    let BMID = massPersonDetailsD * massPersonHeightD
    if (BMID > BMIR) {
        console.log("The BMI of Dan is " + BMID + "he must be a regime !")
    } else {
        console.log("The BMI of Raphael is " + BMIR + "he must be a regime !")
    }

}