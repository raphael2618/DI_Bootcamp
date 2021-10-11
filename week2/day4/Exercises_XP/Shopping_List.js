//Add the stock and prices objects to your js file.
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppingList = ["banana","orange","apple","blueberry"];
let price =0;
const myBill = () =>{
    for(let article of shoppingList){
        if(article in stock && stock[article]>0){
            price+= prices[article];
            //Bonus
            stock[article]--;
        }
    }
    console.log("The total price is : " + price);
    console.log(stock);
}
myBill();
// console.log(stock.apple,stock.banana,stock.orange)
