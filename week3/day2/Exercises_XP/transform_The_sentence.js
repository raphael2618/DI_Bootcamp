// Create a function called getBold_items() that takes no parameter.
// This function should collect all the bold items inside the paragraph.

function getBold_Items() {
    let strongElements = document.querySelectorAll('strong');
    for (let i = 0; i < strongElements.length; i++) {
        let strongValue = strongElements[i].textContent;
        // console.log(strongValue)
        let array = []
        array.push(strongValue)
        return strongValue
    }

}
getBold_Items()


//     Create a function called highlight() that changes the color of all the bold text to blue.
function highlight(color) {
    let Bold_values_result =getBold_Items()
    console.log(Bold_values_result )
    for(let i=0;i<strongValue.length;i++) {
        let c = strongValue[i]
        c.style.color=color
    }
}
highlight()
//     Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal() {
    highlight("black")

}

//     Call the function highlight() v (ie. when the mouse pointer is moved onto the paragraph),
//     and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example for (let i = 0; i < paragraphe.length; i++) {
let result_H = highlight()
let bold_result = getBold_Items()
let return_Normal_Result = return_normal()
let strongElements = document.querySelectorAll('strong');

bold_result.addEventListener("onmouseover", function () {
        for (let i = 0; i < strongElements.length; i++) {
            result_H
        }
    })

return_Normal_Result.addEventListener("onmouseout", function () {
    for (let i = 0; i < strongElements.length; i++) {
        return_Normal_Result
    }
})

