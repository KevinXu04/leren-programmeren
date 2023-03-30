let button = document.createElement("button");
let kopje = document.querySelector("h1");
let name = "Kevin";
button.innerText = "test";
teller = 0;

document.body.appendChild(button);

button.style.width = "100px";
button.style.height = "100px";
button.style.backgroundColor = "blue";
button.style.color = "white";

button.addEventListener("mouseover", function handleMouseOver(){
    button.style.backgroundColor = "red";
    button.style.textDecoration = "underline";
})

button.addEventListener("mouseout", function handleMouseOut(){
    button.style.backgroundColor = "blue";
    button.style.textDecoration = "none";
})

button.addEventListener("click", function click(){
    kopje.innerText = `Welkom ${name}`;
    teller += 1;

    if (teller == 2){
        button.style.visibility = "hidden";
    }
})

// let button = document.createElement("button");
// button.innerText = "test";
// button.className = 'button1';

// document.body.appendChild(button);

