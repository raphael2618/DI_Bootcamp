
let planets = 'Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune'.split(',');
let backgroundColor = ["blue","lightblue","white","orange","red","yellow","green","grey","purple"];
for (let i in planets) {
    let newDiv = document.createElement('div');
    newDiv.id = planets[i];
    newDiv.className = "planet";
    newDiv.innerHTML = planets[i];
    let newColor = newDiv.style.background = backgroundColor[i];
    document.body.appendChild(newDiv);
}










