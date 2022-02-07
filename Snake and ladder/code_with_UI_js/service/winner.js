const restartGame = () => {
  location.reload();
};

export const winner = (player) => {
  document.getElementById("moveInfo").innerHTML = "";
  document.getElementById("moveInfo").innerHTML += player.name + " won";
  document.getElementById("moveBtn").innerHTML = "";
  document.getElementById("moveBtn").innerHTML = "Restart Game";
  document.getElementById("triggerModalBtn").click();
  document.getElementById("moveBtn").onclick = restartGame;
};
