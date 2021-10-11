function findLongestWord(sentence) {
    let arr = sentence.split(" ");
    let longestWord = 0
    for (let i = 0; i < arr.length; i++) {
        if(arr[i].length > longestWord){
            longestWord = arr[i].length;
        }
    }
    return longestWord
}
function wordsInFrame(sentence) {
    let longestWord = findLongestWord(sentence)+4;
    let myArr = sentence.split(" ");
    let star = "*";
    console.log(star.repeat(longestWord));
    for (let i = 0; i < myArr.length; i++) {
        let numOfRepetition = longestWord - myArr[i].length -3;
        console.log("* "+ myArr[i] + " ".repeat(numOfRepetition) +"*");
    }
    console.log(star.repeat(longestWord));
}