
    //Prompt the user for the first number.
    let num1 = parseInt(prompt("Enter a first number")) ;
    //Prompt the user for the second number.
    let num2 = parseInt(prompt("Enter a second number"));
//only for to make the calculator real :)
    if (typeof(num1)!="number" || typeof(num2)!="number") {
        alert("Please enter a number." )
    }

    //sum the two numbers
    let sum = num1 + num2;
    //alert the user of the result
    let resultA = alert("the sum of " + num1 + " and " + num2 + " is " + sum)

    //Make a program that can subtract, multiply, and also divide!
    //calculator

    let num1,num2,result,oper;
    num1=prompt("Type first number");
    num2=prompt("Type second number");
    oper=prompt("Type an operator");

    if(oper=="+"){
        result=Number(num1)+Number(num2);
    }
    else if(oper=="/"){
        result=Number(num1)/Number(num2);
    }
    else if(oper=="*"){
        result=Number(num1)*Number(num2);
    }
    else if(oper=="-"){
        result=Number(num1)-Number(num2);
    }

    alert(result)
