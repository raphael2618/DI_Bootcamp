let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
// Create a function called checkBasket().
//     It should:
//     prompt the user for an item
function checkBasket() {
    let item = console.log("Enter an item")
    // let the user know if the item is in the basket
    if(item in amazonBasket) {
        console.log("your item is in the basket." )
    } else {
        console.log("your item is not in the basket" )
    }

}