function equal() {
    let p = document.getElementById("result").value;
    let q = eval(p);
    document.getElementById("result").value = q;


}


function clearScreen() {
    document.getElementById("result").value = "";
}

function display(value) {
    document.getElementById("result").value += value;
}
function reset() {
    document.getElementById("result").value =0;
}