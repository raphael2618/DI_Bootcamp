
let planets = 'Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune'.split(',');
for (let i in planets) {
    let newDiv = document.createElement('div');
    newDiv.id = planets[i];
    newDiv.className = "planet";
    newDiv.innerHTML = planets[i];
    document.body.appendChild(newDiv);

}

document.getElementById("Mercury").style.backgroundColor="blue"
document.getElementById("Venus").style.backgroundColor="green"
document.getElementById("Earth").style.backgroundColor="red"
document.getElementById("Mars").style.backgroundColor="orange"
document.getElementById("Jupiter").style.backgroundColor="purple"
document.getElementById("Saturn").style.backgroundColor="green"
document.getElementById("Uranus").style.backgroundColor="yellow"
document.getElementById("Neptune").style.backgroundColor="brown"










