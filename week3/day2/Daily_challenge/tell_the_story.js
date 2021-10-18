let inputValue = document.getElementsByTagName("input")
let btn = document.getElementById("lib-button")
btn.addEventListener("click", function () {
    let verbD = document.getElementById("verb").value
    let nounD = document.getElementById("noun").value
    let placeD = document.getElementById("place").value
    let adjectiveD = document.getElementById("adjective").value
    let personD = document.getElementById("person").value
    if(verbD==""||nounD==""||placeD==""||adjectiveD==""||personD=="") {
        alert("Fill all the input of the form.")
    }
    let streetValue = inputValue.place.value
    let onS=""
    if(streetValue==="street") {onS=" on "} else {onS=" in "}
    let strIng = "ing "
    let newVerb = inputValue.verb.value + strIng
    let personEl = inputValue.person.value
    let strPluriel = " "
    if (personEl.split(" ").length > 1) {
        strPluriel = " they are "
    } else { strPluriel = " is "}

    let spanStory = document.getElementById("story")
    spanStory.innerHTML="The story of " + inputValue.person.value + " and " + "the " + inputValue.adjective.value + " " + inputValue.noun.value + " that" + strPluriel + newVerb + onS  + inputValue.place.value
})

// //to test the programme, you can give default value to the input.
// let verbD = document.getElementById("verb").defaultValue="find"
// let nounD = document.getElementById("noun").defaultValue="job"
// let placeD = document.getElementById("place").defaultValue="company"
// let adjectiveD = document.getElementById("adjective").defaultValue="good"
// let personD = document.getElementById("person").defaultValue="fayga raphael"



