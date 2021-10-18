let eventEl = document.getElementById("event")
let btn = document.getElementById("button")
btn.addEventListener("click", function () {
    eventEl.innerText="Hello"
    eventEl.style.color="red"
    eventEl.style.fontSize="15px"
    eventEl.style.fontWeight="bold"
    eventEl.style.cursor="pointer"
    eventEl.style.border="1px solid black"
    eventEl.style.margin="5px"
    eventEl.style.backgroundColor="blue"
    eventEl.title="Test"
    eventEl.classList.add("test")



})