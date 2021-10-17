// let table = document.body.firstElementChild;
let array = [{
    title :"Harry Potter",
    author : "JK Rolling",
    image : "https://images-na.ssl-images-amazon.com/images/I/91ocU8970hL.jpg",
    alreadyRead : true
}, {
        title :"Hunger Games",
        author : "Suzanne Collins",
        image : "https://images-na.ssl-images-amazon.com/images/I/61i8nC90deL.jpg",
        alreadyRead : true
}]

let listBooksEl = document.getElementById("listBooks")

tbl = document.createElement('table');
tbl.style.width = '100px';
tbl.style.border = '1px solid black';

for (let i = 0; i < array.length; i++) {
    const tr = tbl.insertRow();
    for (let j = 0; j < 2; j++) {
        if (i === 2 && j === 1) {
            break;
        }
    }
}
listBooksEl.appendChild(tbl);