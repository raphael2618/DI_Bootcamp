

    //with nested function
    for(let i=1; i<=5; i++){
        console.log("* ".repeat(i));
    }
    //Without nested function
    let n = 5;
    let string = "";
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            string += "* ";
        }
        string += "\n";
    }
    console.log(string);
