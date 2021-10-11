function isDivisible() {
    let results = [];
    let firstNumber = 0;
    let secondNumber = 500;
//put all the numbers divide by 23 in an array
    for (var arrayy = firstNumber; arrayy < secondNumber; arrayy++) {
        if (arrayy % 23 === 0) {
            results.push(arrayy);
        }
    }
    //calculate the sum of the array and console log the results of the array and the sum.
    var sum = 0;
    for (var i = 0; i < results.length; i++) {
        sum += results[i];
    }
    console.log(results);
    console.log(sum)


    }

    isDivisible()