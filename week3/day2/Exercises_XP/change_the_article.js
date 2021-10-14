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
let NameInput =  document.getElementById("fname").value
let LastNameInput =  document.getElementById("lname").value
btnForm.addEventListener("click", function () {
    if(NameInput==='' || LastNameInput==='') {
        //display everytime
        alert("Input empty. Fill all the input of the form.")
    }
})
document.body.appendChild(btnForm);

    tbl  = document.createElement('table');

    let row = tbl.insertRow(0);
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    cell1.textContent = NameInput;
    cell2.textContent = LastNameInput;
    document.body.appendChild(tbl);

