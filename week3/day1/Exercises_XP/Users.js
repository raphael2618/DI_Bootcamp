// In the HTML above change the name “Pete” to “Richard”.
liEl = document.getElementsByTagName('li')
liEl[1].innerText ="Richard"

// Change each first name of the two <ul>'s to your name.
let liElement = document.getElementsByTagName('ul > li')
let ulElement = document.getElementById("list")
for(let i =0;i<2;i++) {
    ulElement[i].innerText="Raphael"
}

// document.getElementsByTagName("li")[0]="raphael"
// At the end of each <ul> add a <li> that says “Hey students”.
let newli = document.createElement("li")
let nodeD =document.createTextNode("Hello Student")
newli[0].appendChild(nodeD)

// Delete the name Sarah from the second <ul>.
let SarahPos = document.getElementsByTagName("li")[3]
SarahPos.parentElement.removeChild(SarahPos)
ulElement.parentElement.firstElementChild
// Bonus
// Add a class called student_list to both of the <ul>'s.
document.getElementsByTagName('ul > li:firstChild')

ulElement.classList.add("student_list")

// Add the classes university and attendance to the first <ul>.



