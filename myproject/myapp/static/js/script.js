// Puzzle kutularını seçin
const boxes = document.querySelectorAll('.game-box');

// Oyun başlamadan önce kutulara rastgele sayılar yerleştirin
function shuffleBoxes() {
  const numbers = Array.from({length: 16}, (_, i) => i + 1);
  const shuffledNumbers = numbers.sort(() => Math.random() - 0.5);
  boxes.forEach((box, index) => {
    box.textContent = shuffledNumbers[index];
  });
}

// Oyunu başlatmak için bir event listener ekleyin
const startButton = document.querySelector('#start-button');
startButton.addEventListener('click', startGame);

// Oyuna başladığınızda, süre sayaç ve hamle sayaçları oluşturun
function startGame() {
  let time = 0;
  let moves = 0;
  const timerElement = document.querySelector

  // Oyunu başlatmak için bir event listener ekleyin
const startButton = document.querySelector('#start-button');
startButton.addEventListener('click', startGame);

// Oyuna başladığınızda, süre sayaç ve hamle sayaçları oluşturun
function startGame() {
  let time = 0;
  let moves = 0;
  const timerElement = document.querySelector('#timer');
  const movesElement = document.querySelector('#moves');

  // Saniye bazında süre sayacı oluşturun
  const timerInterval = setInterval(() => {
    time++;
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    const formattedTime = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    timerElement.textContent = `Süre: ${formattedTime}`;
  }, 1000);
  }

  // Kutulara click event listener ekleyin
  boxes.forEach((box) => {
    box.addEventListener('click', () => {
      // Boş kutu pozisyonunu alın
      const emptyBox = document.querySelector('.game-box-empty');
      const emptyIndex = Array.from(boxes).indexOf(emptyBox);

      // Tıklanan kutu pozisyonunu alın
      const clickedIndex = Array.from(boxes).indexOf(box);

      // Kutuların konumunu değiştirin
      const isAdjacent = getAdjacentIndices(emptyIndex).includes(clickedIndex);
      if (isAdjacent) {
        swapBoxes(emptyBox, box);
        moves++;
        movesElement.textContent = `Hamle: ${moves}`;

        // Oyun bitti mi diye kontrol edin
        const isGameComplete = checkGameComplete();
        if (isGameComplete) {
          clearInterval(timerInterval);
          alert(`Tebrikler! ${time} saniyede ${moves} hamle ile oyunu tamamladınız.`);
        }
      }
    });
  });

  // Kutuların konumlarını değiştirmek için yardımcı fonksiyonlar
  function getAdjacentIndices(index) {
    const isLeftEdge = (index % 4 === 0);
    const isRightEdge = (index % 4 === 3);
    const isTopEdge = (index < 4);
    const isBottomEdge = (index > 11);
    const adjacentIndices = [];
    if (!isLeftEdge) adjacentIndices.push(index - 1);
    if (!isRightEdge) adjacentIndices.push(index + 1);
    if (!isTopEdge) adjacentIndices.push(index - 4);
    if (!isBottomEdge) adjacentIndices.push(index + 4);
    return adjacentIndices;
  }

  function swapBoxes(box1, box2) {
    [box1.textContent, box2.textContent] = [box2.textContent, box1.textContent];
    [box1.classList, box2.classList] = [box2.classList, box1.classList];
  }

  function checkGameComplete() {
    const numbers = Array.from({length: 16}, (_, i) => i + 1);
    const currentNumbers = Array.from(boxes).map(box => Number(box.textContent));
    return numbers.every((number, index) => number === currentNumbers[index]);
  }
}
