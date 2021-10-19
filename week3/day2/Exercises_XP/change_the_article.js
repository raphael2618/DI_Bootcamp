let paragraph_element = document.getElementsByTagName("p")[3]
paragraph_element.remove()
let button = document.querySelector("h2");

button.addEventListener("click",function(){
    this.style.backgroundColor = "red";});

button.addEventListener("mouseover",function(){
    this.style.cursor = "pointer";});

let h1element = document.querySelector("h1")
let randomNumber = Math.floor(Math.random() * 101)
h1element.style.fontSize= randomNumber+"px"

let h3element = document.querySelector("h3");
h3element.addEventListener("click", function () {
    this.style.display = "none";});

let btn = document.createElement("button");
btn.innerHTML = "Nouveau";
btn.style.backgroundColor="Blue"
btn.style.fontSize= 13

let paragraphe = document.querySelectorAll("p");

for (let i = 0; i < paragraphe.length; i++) {
    btn.addEventListener("click", function() {
        paragraphe[i].style.fontWeight="bold"
    });
}
document.body.appendChild(btn);

let btnForm =document.getElementById("submit")
let NameInput =  document.getElementById("fname")
let LastNameInput =  document.getElementById("lname")
btnForm.addEventListener("click", function () {
    if( LastNameInput.value===''||NameInput.value==='') {
        alert("Input empty. Fill all the input of the form.")
    }

    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');


// Adding the entire table to the body tag
    let UserAnswer = document.getElementsByClassName("usersAnswer")[0]
// Creating and adding data to first row of the table
    let row_1 = document.createElement('tr');
    let heading_2 = document.createElement('th');
    heading_2.innerHTML = "Name";
    let heading_3 = document.createElement('th');
    heading_3.innerHTML = "Last name";

    row_1.appendChild(heading_2);
    row_1.appendChild(heading_3);
    thead.appendChild(row_1);

// Creating and adding data to second row of the table
    let row_2 = document.createElement('tr');
    let row_2_data_2 = document.createElement('td');
    row_2_data_2.innerHTML = LastNameInput.value ;
    let row_2_data_3 = document.createElement('td');
    row_2_data_3.innerHTML = NameInput.value;

    row_2.appendChild(row_2_data_2);
    row_2.appendChild(row_2_data_3);
    tbody.appendChild(row_2);


    table.appendChild(thead);
    table.appendChild(tbody);


    let row = UserAnswer.insertRow(0);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    cell1.innerHTML = LastNameInput.value;
    cell2.innerHTML = NameInput.value;

    UserAnswer.appendChild(table)
    NameInput.value="";
    LastNameInput.value="";



})
document.body.appendChild(btnForm)

let sec_Paragraphe = document.getElementById("par2")
sec_Paragraphe.addEventListener("mouseover", function() {
    this.style.  opacity= "1";
    this.style.transition="opacity 1000ms";
})



