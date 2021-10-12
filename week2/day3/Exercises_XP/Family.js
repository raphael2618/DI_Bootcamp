
let Family = {
    Name: "aaron",
    LastName: "yaacovich",
    Email:"boussidan.raphael@gmail.com",
    mass:60
};

const keyss = Object.keys(Family),valuess = Object.values(Family);
console.log(
    keyss.toString().replace(",", "\t") +
    "\n" +
    valuess.toString().replace(",", "\t")
);

for(let i in Family){
    console.log("The keys are " + i); // alerts key
    console.log("The values are " + Family[i]); //alerts key's value
}