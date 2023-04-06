// DOM Elements
const puzzleContainer = document.querySelector('.puzzle-container');
const inputImage = document.querySelector('#inputImage');
const btnStart = document.querySelector('#btnStart');
const timer = document.querySelector('.timer');
const moves = document.querySelector('.moves');
const congratsModal = document.querySelector('.congrats-modal');
const congratsMsg = document.querySelector('#congratsMsg');

// Variables
let timerInterval;
let seconds = 0;
let minutes = 0;
let movesCount = 0;
let emptyBlock;
let puzzleBlocks;

// Event Listeners
inputImage.addEventListener('change', (e) => {
  const file = e.target.files[0];
  const url = URL.createObjectURL(file);
  createPuzzle(url);
});

btnStart.addEventListener('click', () => {
  startGame();
});

// Functions
function createPuzzle(url) {
  // Resize image and split into pieces
  // ...

  // Create puzzle blocks
  // ...

  // Shuffle puzzle blocks
  // ...

  // Add blocks to container
  // ...
}

function startGame() {
  // Start timer
  // ...

  // Enable puzzle blocks to be draggable
  // ...

  // Increment moves count
  // ...

  // Check if puzzle is solved
  // ...
}

function stopTimer() {
  // Stop timer interval
  // ...
}

function shuffle(array) {
  // Shuffle array
  // ...
}

function moveBlock(block) {
  // Move block to empty space
  // ...
}

function checkSolved() {
  // Check if puzzle is solved
  // ...
}

function showCongratsModal() {
  // Show congrats modal
  // ...
}

function hideCongratsModal() {
  // Hide congrats modal
  // ...
}

function resetGame() {
  // Reset game variables
  // ...

  // Reset puzzle container
  // ...
}

// Puzzle tahtası için gerekli değişkenlerin oluşturulması
var puzzleSize = 4;  // 4x4'lük bir tahta olacak
var tileSize = 100; // Her kare 100x100 piksel olacak
var tileSpacing = 10; // Kareler arasında 10 piksel boşluk olacak

// Tahtanın boyutuna uygun canvas elementinin oluşturulması
var canvas = document.createElement('canvas');
canvas.width = puzzleSize * (tileSize + tileSpacing) + tileSpacing;
canvas.height = puzzleSize * (tileSize + tileSpacing) + tileSpacing;
document.getElementById('game-board').appendChild(canvas);

// Canvas elementi için context'in oluşturulması
var ctx = canvas.getContext('2d');

// Resim yükleme işlemi
var img = new Image();
img.onload = function() {
  // Resim başarılı bir şekilde yüklendiğinde çalışacak kod bloğu
  // Puzzle parçalarının oluşturulması
  var tiles = [];
  for (var i = 0; i < puzzleSize; i++) {
    for (var j = 0; j < puzzleSize; j++) {
      var tile = {};
      tile.sx = j * (tileSize + tileSpacing) + tileSpacing;
      tile.sy = i * (tileSize + tileSpacing) + tileSpacing;
      tile.dx = i * (tileSize + tileSpacing) + tileSpacing;
      tile.dy = j * (tileSize + tileSpacing) + tileSpacing;
      tile.width = tileSize;
      tile.height = tileSize;
      tiles.push(tile);
    }
  }
  
  // Resmin parçalara ayrılması
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  for (var i = 0; i < tiles.length; i++) {
    var tile = tiles[i];
    tile.imgData = ctx.getImageData(tile.sx, tile.sy, tileSize, tileSize);
    ctx.clearRect(tile.sx, tile.sy, tileSize, tileSize);
  }
  
  // Puzzle parçalarının karıştırılması
  for (var i = 0; i < tiles.length; i++) {
    var j = Math.floor(Math.random() * tiles.length);
    var temp = tiles[i];
    tiles[i] = tiles[j];
    tiles[j] = temp;
  }
  
  // Karıştırılmış puzzle parçalarının tahta üzerine çizdirilmesi
  for (var i = 0; i < tiles.length; i++) {
    var tile = tiles[i];
    ctx.putImageData(tile.imgData, tile.dx, tile.dy);
    tile.x = tile.dx;
    tile.y = tile.dy;
    tile.correctX = tile.dx;
    tile.correctY = tile.dy;
  }
  
  // Puzzle tahtasının tıklanabilir hale getirilmesi
  canvas.addEventListener('click', function(event) {
    var mouseX = event.offsetX;
    var mouseY = event.offsetY;
    for (var i = 0; i < tiles.length; i++) {
      var tile = tiles[i];
      if (tile.x < mouseX && tile.x + tileSize > mouseX && tile.y < mouseY && tile.y + tileSize > mouseY) {
        // Seçilen parçanın hare
        function swapTiles(cell1,cell2) {
            var temp = document.getElementById(cell1).className;
            document.getElementById(cell1).className = document.getElementById(cell2).className;
            document.getElementById(cell2).className = temp;
          }
          
          function shuffle() {
            //Use nested loops to access each cell of the 4x4 grid
            for (var row=1;row<=4;row++) { //For each row of the 4x4 grid
              for (var column=1;column<=4;column++) { //For each column in this row
              
                var row2=Math.floor(Math.random()*4 + 1); //Pick a random row from 1 to 4
                var column2=Math.floor(Math.random()*4 + 1); //Pick a random column from 1 to 4
                 
                swapTiles("cell"+row+column,"cell"+row2+column2); //Swap the look & feel of both cells
              } 
            } 
          }
          
          function clickTile(row,column) {
            var cell = document.getElementById("cell"+row+column);
            var tile = cell.className;
            if (tile!="tile16") { 
                 //Checking if white tile on the right
                 if (column<4) {
                   if ( document.getElementById("cell"+row+(column+1)).className=="tile16") {
                     swapTiles("cell"+row+column,"cell"+row+(column+1));
                     return;
                   }
                 }
                 //Checking if white tile on the left
                 if (column>1) {
                   if ( document.getElementById("cell"+row+(column-1)).className=="tile16") {
                     swapTiles("cell"+row+column,"cell"+row+(column-1));
                     return;
                   }
                 }
                   //Checking if white tile is above
                 if (row>1) {
                   if ( document.getElementById("cell"+(row-1)+column).className=="tile16") {
                     swapTiles("cell"+row+column,"cell"+(row-1)+column);
                     return;
                   }
                 }
                 //Checking if white tile is below
                 if (row<4) {
                   if ( document.getElementById("cell"+(row+1)+column).className=="tile16") {
                     swapTiles("cell"+row+column,"cell"+(row+1)+column);
                     return;
                   }
                 } 
            }   
          }
        }
      }
    } 
