// Number of lines for the alphabet's pattern
let height = 5;
// Number of character width in each line
let width = (2 * height) - 1;

// Function to print the pattern of 'A'
const printA = () => {
    let n = parseInt(width / 2), i, j;
    for (i = 0; i < height; i++) {
        for (j = 0; j <= width; j++) {
            if (j == n || j == (width - n)
                || (i == parseInt(height / 2) && j > n
                    && j < (width - n)))
                //write on the page
                document.write("*");
            else
                document.write("  ");
        }
        document.write(`<br/>`);
        n--;
    }
}

printA()