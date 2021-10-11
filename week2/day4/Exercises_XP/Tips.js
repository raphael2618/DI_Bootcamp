//     Ask John for the amount of the bill.
let bill=prompt("Enter the amount of the bill please")
//     Create the program explained above.

// Tip 20% when the bill is less than $50,
if(bill<50) {
    var tip=0.2;
}
//     2. Tip 15% when the bill is between $50 and $200,
else if(bill>50 && bill<200) {
    var tip=0.15;
}
//     3. Tip 10% if the bill is more than $200.
else if(bill>200) {
    var tip=0.10;
}

//     In the end, John would like to know:
//     Tip amount.
let totalTips = bill * tip;
console.log("The amount of the bill is : " + totalTips )
//     Final bill (bill + tip).
let finalValues = bill + bill * tip;
console.log("The amount of the final bill is : " + finalValues )

