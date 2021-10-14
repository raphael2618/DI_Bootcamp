function Validate() {
    let charactersOnly = document.getElementById("letters").value;
    if (charactersOnly.search(/^[a-zA-Z]+$/) === -1) {
        alert("Only characters");
        document.getElementById('letters').value = "";
    }
}