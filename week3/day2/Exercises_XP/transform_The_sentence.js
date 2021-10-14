// Create a function called getBold_items() that takes no parameter.
// This function should collect all the bold items inside the paragraph.

function getBold_Items() {
    let strongElements = document.querySelectorAll('strong');
    for (let i = 0; i < strongElements.length; i++) {
        let strongValue = strongElements[i].innerText;
        // console.log(strongValue)
        let array = []
        array.push(strongValue)
        console.log(array)
    }

}
getBold_Items()


//     Create a function called highlight() that changes the color of all the bold text to blue.
function highlight() {
    getBold_Items()
    let Bold_values_result =getBold_Items()
    Bold_values_result.style.color="blue"

}
highlight()
//     Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal() {

}
//     Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this examplefor (let i = 0; i < paragraphe.length; i++) {
