function shuffle(array) {
    let currentIndex = array.length, randomIndex;

    while (currentIndex != 0) {

        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }

    return array;
}

const cardsData = [
    {name:"lion", imgSrc: "lion.png", id: "1"},
    {name:"lobster", imgSrc: "lobster.png", id: "2"},
    {name:"seagull", imgSrc: "seagull.png", id: "3"},
    {name:"skunk", imgSrc: "skunk.png", id: "4"},
    {name:"turtle", imgSrc: "turtle.png", id: "5"},
    {name:"bear", imgSrc: "bear.png", id: "6"},
    {name:"deer", imgSrc: "deer.png", id: "7"},
    {name:"frog", imgSrc: "frog.png", id: "8"},
    {name:"horse", imgSrc: "horse.png", id: "9"},
    {name:"tiger", imgSrc: "tiger.png", id: "10"}
];

let buttonsContainer = document.getElementById("buttons");
let imagesContainer = document.getElementById("images");

let cards = shuffle(cardsData);
console.log(cards);

for (i = 0; i < cards.length; i++) {
    let button = document.createElement("button");

    console.log(button.id);

    button.innerText = cards[i].name;
    let image = document.createElement("img");
    image.src = "images/background.png";
    button.addEventListener("click", function(){
        image.src = `images/${cards[i].name}.png`;
    });

    button.appendChild(image);
    buttonsContainer.appendChild(button);
}