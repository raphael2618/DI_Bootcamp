let buttonEl = document.getElementById("button")
function myMove() {
    buttonEl.addEventListener("click", function () {
        let e = document.getElementById("animate");
        let s = 1;
        setInterval(function(){
            let eLeftPos = e.offsetLeft;
            e.style.left = (eLeftPos + s) + 'px';

        }, 1000);

    })
}

myMove()