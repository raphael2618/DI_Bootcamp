// In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation,
// using the setAttribute method.
let idValue = document.getElementById("navBar")
idValue.setAttribute("id","socialNetworkNavigation")


//     We are going to add a new <li> to the <ul>.
let ul=document.getElementsByTagName("ul")

// First, create a new <li> tag (use the createElement method).
let li = document.createElement("li");

// Create a new text node with “Logout” as its specified text.
//Append the text node to the newly created list node (li).
let newVar=li.appendChild(document.createTextNode("Logout"));

//     Finally, append this updated list node to the unordered list above, using the appendChild method.
ul[0].appendChild(newVar)

//     Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements
// from their parent element (ul). Display the text of each link. (Hint: use the textContent property).
 console.log(li.firstElementChild ).textContent
 console.log(ul.lastElementChild ).textContent
