let strong = document.querySelectorAll("strong")
console.log(strong)
function getBold (){
    let getStrong = document.querySelectorAll("strong")
    console.log(getStrong)
}
getBold()

function highlight() {
    for (i = 0; i < strong.length; i++) {
        strong[i].style.color = "blue";
    }
}
function return_normal(){
    notbold = document.getElementsByTagName("p")[0];
    for(let i = 0 ; i < notbold.childElementCount;i++){
        notbold.children[i].style.fontWeight="normal";
        notbold.children[i].style.color="black";
    }
}
let p = document.getElementsByTagName("P")[0];
p.addEventListener("mouseover",highlight);
p.addEventListener("mouseout",return_normal);
