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

//Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”.
let shoppingList =["banana","orange","apple"]
// Create a function called myBill() that takes no parameters.
function myBill() {
    if(stock.orange>0 ||stock.banana>0||stock.apple>0) {
        let  bananaPrice =1 * prices.banana
        let  applePrice =1* prices.apple
        let  orangePrice =1 * prices.orange
        let totalCart = bananaPrice + applePrice + orangePrice
        console.log("total cart :" + totalCart )
    } else {
        console.log("Item not in stock.")
    }
    for (let i in stock) {
        if(stock[i]>0) {
            let stockDecrease=0;
            stockDecrease= stock[i]-1
        }
    }

}
// console.log(stock.apple,stock.banana,stock.orange)
myBill()

