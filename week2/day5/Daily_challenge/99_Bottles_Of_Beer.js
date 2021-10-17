let userPrompt = prompt('Welcome to the "99 Bottles of Beer" song!\nEnter a number:');

const isValidNum = (numberV) => numberV !== undefined && numberV !== null && numberV.length > 0 && !isNaN(numberV);

while (!isValidNum(userPrompt)) userPrompt = prompt('InuserPromptalid try again?!\nEnter a number:');

const sing = (userPrompt) => {

    let total = userPrompt;

    for (let i = 1; i <= total; i++) {
        console.log(`${total} ${total > 1 ? 'bottles' : 'bottle'} of beer on the wall`);
        console.log(`${total} ${total > 1 ? 'bottles' : 'bottle'} of beer`);
        console.log(`Take ${i} down, pass ${i > 1 ? 'them' : 'it'} around`);
        total -= i;
        console.log(`${total - i < 1 ? 'Not enough' : total > 1 ? 'bottles' : 'bottle'} bottles of beer on the wall`);
    }
    console.log(`Not enough bottles of beer on the wall`);
    console.log(`Not enough bottles of beer`);
    console.log(`Go to the store and buy some more`);
    console.log(`${userPrompt} bottles of beer on the wall`);
}


sing(Number(userPrompt));
