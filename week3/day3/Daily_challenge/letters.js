function Validate(e) {
    //i use a deprecated method i know ...
    let keyCode = e.keyCode || e.which;

    let lblError = document.getElementById("lblError");
    lblError.innerHTML = "";

    //Regex for Valid Characters i.e. Alphabets.
    let regex = /^[A-Za-z]+$/;

    //Validate TextBox value against the Regex.
    let isValid = regex.test(String.fromCharCode(keyCode));
    if (!isValid) {
        lblError.innerHTML = "Only Alphabets allowed.";
    }

    return isValid;
}
