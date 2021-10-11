
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
}
let nameObject=prompt("What is your name ?")
if(nameObject in guestList) {
    console.log( "Hi! I'm " + nameObject  + " and I'm from " + guestList[nameObject])
}
