var bottles = prompt("Enter number to begin counting down bottles");
for (var counter = 99; counter >= 1; counter = counter - 1)
{
    if (counter == 1) {
        bottles = 'bottle';
    } else {
        bottles = 'bottles';
    }
    console.log(counter+" "+bottles+" of beer on the wall.");
    if (counter < 99) {
        console.log("");
        console.log(counter+" "+bottles+" of beer on the wall.");
    }
    console.log(counter+" "+bottles+" of beer.");
    /*for(let i<counter;i=0;i++) {
        let numberTake=numberTake+i;
        console.log("Take" +numberTake + "down.");
}*/
        console.log("Take one down" )
    console.log("Pass it around.");
    if (counter == 1) {
        console.log("No bottles of beer on the wall.");
    }
}