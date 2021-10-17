
// In the HTML above change the name “Pete” to “Richard”.
let liEl = document.getElementsByTagName('li')
liEl[1].innerText ="Richard"

// Change each first name of the two <ul>'s to your name.
let liJohn = document.getElementsByTagName('li')[0]
let liDavid = document.getElementsByTagName('li')[2]
let ulElement = document.getElementById("list")
liJohn.innerText="raphael"
liDavid.innerText="raphael"

// document.getElementsByTagName("li")[0]="raphael"
// At the end of each <ul> add a <li> that says “Hey students”.
let newli = document.createElement("li")
let nodeD =document.createTextNode("Hello Student")
newli.appendChild(nodeD)

// Delete the name Sarah from the second <ul>.
let SarahPos = document.getElementsByTagName("li")[3]
SarahPos.parentElement.removeChild(SarahPos)

// Bonus
// Add a class called student_list to both of the <ul>'s.
liJohn.classList.add("student_list")
liDavid.classList.add("student_list")

// Add the classes university and attendance to the first <ul>.
let listItems = document.querySelectorAll('ul > li');
liJohn.classList.add("attendance")
liDavid.classList.add("university")




