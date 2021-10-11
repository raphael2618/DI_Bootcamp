
const anObj = { 100: 'a', 2: 'b', 7: 'c' };
Object.entries(anObj).forEach(([key, value]) => {
    console.log(`${key} ${value}`);
});
