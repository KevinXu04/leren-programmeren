const imageData = [
    "images/default1.png", 
    "images/default2.png", 
    "images/travis.png", 
    "images/llamga.png", 
    "images/fish.png", 
];

let count = 0;
let previous = document.getElementById("previous");
let next = document.getElementById("next");

let image = document.getElementById("image");

next.addEventListener("click", function click(){
    if (count == imageData.length-1){
        count = 0
    } else {
        count += 1;
    }
    image.src = imageData[count];
})

previous.addEventListener("click", function click(){
    if (count == 0){
        count = imageData.length - 1
    } else{
        count -= 1;
    }
    image.src = imageData[count];
    
})