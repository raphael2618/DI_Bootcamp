const changeEnough = (arr, bill) => {
    let quarter = arr[0] * 0.25;
    let dime = arr[1] * 0.1;
    let nickel = arr[2] * 0.05;
    let penny = arr[3] * 0.01;
    if ((quarter + dime + nickel + penny) >= bill) {
        return true;
    } else return false;
};

console.log(changeEnough([2, 100, 0, 0], 14.11));
console.log(changeEnough([0, 0, 20, 5], 0.75));