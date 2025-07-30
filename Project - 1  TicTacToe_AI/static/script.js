let board = Array(9).fill(0);
let gameOver = false;

function renderBoard() {
  const boardDiv = document.getElementById("board");
  boardDiv.innerHTML = "";
  board.forEach((cell, index) => {
    const box = document.createElement("div");
    box.className = "cell";
    box.innerText = cell === 1 ? "❌" : cell === 2 ? "⭕" : "";
    if (!gameOver && cell === 0) {
      box.onclick = () => makeMove(index);
    }
    boardDiv.appendChild(box);
  });
}

function makeMove(index) {
  if (board[index] !== 0 || gameOver) return;
  board[index] = 1;
  fetch("/move", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ board }),
  })
  .then(res => res.json())
  .then(data => {
    board = data.board;
    renderBoard();
    if (data.status === "end") {
      gameOver = true;
      showWinner(data.winner);
    }
  });
}

function showWinner(winner) {
  const modal = document.getElementById("winnerModal");
  const msg = document.getElementById("winnerMessage");
  msg.innerText = winner === 1 ? "🎉 You Win!" : winner === 2 ? "💻 AI Wins!" : "🤝 It's a Tie!";
  modal.style.display = "block";
}

function closeModal() {
  document.getElementById("winnerModal").style.display = "none";
}

function resetGame() {
  board = Array(9).fill(0);
  gameOver = false;
  renderBoard();
  closeModal();
}

renderBoard();
