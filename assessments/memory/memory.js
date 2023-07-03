function shuffle(array) {
    let currentIndex = array.length, randomIndex;

    while (currentIndex != 0) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }

    return array;
}

let animalLst = ["lion", "lobster", "seagull", "skunk", "turtle", "bear", "deer", "frog", "horse", "tiger"];
let test = [];
let firstCard, secondCard;
let activeCard = false;

let buttonsContainer = document.getElementById("buttons");
let imagesContainer = document.getElementById("images");

let firstRow = document.createElement("div");
let secondRow = document.createElement("div");

animalLst = shuffle(animalLst);

for (let i = 0; i < animalLst.length; i++){
    let button = document.createElement("button");
    button.id = animalLst[i];

    test.push(animalLst[i]);

    console.log(button.id);

    button.innerText = animalLst[i];
    let image = document.createElement("img");
    image.src = "images/background.png";
    button.addEventListener("click", function(){
        activeCard = true;
        image.src = `images/${animalLst[i]}.png`;
        firstCard = button;
        console.log(firstCard);
    });

    button.appendChild(image);
    firstRow.appendChild(button);
}

let tempLst = shuffle(test);

for (let x = 0; x < tempLst.length; x++){
    let button = document.createElement("button");
    button.innerText = tempLst[x];
    button.id = tempLst[x];
    
    let image = document.createElement("img");
    image.src = "images/background.png";
    button.addEventListener("click", function(){
        image.src = `images/${tempLst[x]}.png`;
        secondCard = button
        if (secondCard.id != firstCard.id) {
            setTimeout(() => {
                image.src = "images/background.png";
            }, 1000);
        }
    });
    
    button.appendChild(image);
    secondRow.appendChild(button);
}

buttonsContainer.appendChild(firstRow);
buttonsContainer.appendChild(secondRow);