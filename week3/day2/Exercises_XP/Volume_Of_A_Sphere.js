//https://www.calculator.net/volume-calculator.html
function calculateVolume(){
    let radius = document.getElementById("radiusID").value;

    let volume = (4/3)* Math.PI * Math.pow(radius, 3);

    alert("The volume of a sphere: "+volume.toFixed(2));
}


let button=document.getElementById("submit");
button.addEventListener("click", function () {
    calculateVolume()
})
