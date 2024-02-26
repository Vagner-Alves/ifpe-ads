const quotes = [
    "A vida é o que acontece enquanto você está ocupado fazendo outros planos. - John Lennon",
    "A única coisa que devemos temer é o próprio medo. - Franklin D. Roosevelt",
    "A imaginação é mais importante que o conhecimento. - Albert Einstein",
    "A felicidade não é algo pronto. Ela vem de suas próprias ações. - Dalai Lama",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia. - Robert Collier"
];

const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];

function randomHexColor(){
  let hexColor = "#";
  for (let i = 0; i < 6; i++) {
    hexColor += hex[Math.floor(Math.random() * hex.length)];
  }

  return hexColor;
}


function clickRandomColorButton(){
  let hexColor = randomHexColor() 
  // minha solução
  const display = document.getElementById('quoteDisplay');
  
  const button = document.getElementById('btn');
  button.addEventListener('click', function onClick(event){
    document.body.style.backgroundColor = hexColor;
    display.innerHTML = quotes[getRandomQuote()];
    
  });
}

function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return randomIndex;
}

