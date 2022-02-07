import { player } from "../model/player.js";
import { checkForLadder } from "./checkLadder.js";
import { checkForSnakes } from "./checkSnakes.js";
import { winner } from "./winner.js";

let player1 = new player();
let player2 = new player();
player1.name = "Green";
player2.name = "Voilet";

let turn_counter = 1;

const setPlayerPostion = () => {
  //moving player 1 green
  if (turn_counter == 1) {
    if (player1.prev_box !== "") {
      document.getElementById(player1.prev_box).removeAttribute("style");
    }
    player1.current_box = "boxTwo" + player1.player_pos;
    document.getElementById(player1.current_box).style =
      "background-color:green;border-radius:20px";
    player1.prev_box = player1.current_box;
    turn_counter = 2;
  }

  //moving player 2 blue
  else if (turn_counter == 2) {
    if (player2.prev_box !== "") {
      document.getElementById(player2.prev_box).removeAttribute("style");
    }
    player2.current_box = "box" + player2.player_pos;
    document.getElementById(player2.current_box).style =
      "background-color:blueviolet;border-radius:20px";
    player2.prev_box = player2.current_box;
    turn_counter = 1;
  }
};

//enable & disable
const disableButton = (x) => {
  const btn = "p" + x;
  document.getElementById(btn).classList.add("disabled");
};
const enableButton = (x) => {
  const btn = "p" + x;
  document.getElementById(btn).classList.remove("disabled");
};

const rollDice = () => {
  let roll = Math.floor(Math.random() * 6) + 1;
  document.getElementById("roll").innerHTML = roll;
  if (turn_counter == 1) {
    let new_pos1 = player1.player_pos + roll;

    if (new_pos1 <= 100) {
      if (new_pos1 == 100) winner(player1);
      disableButton(2);
      enableButton(1);
      new_pos1 = checkForLadder(new_pos1, player1);
      new_pos1 = checkForSnakes(new_pos1, player1);

      player1.player_pos = new_pos1;
      setPlayerPostion();
    } else {
      turn_counter = 2;
    }
  } else if (turn_counter == 2) {
    let new_pos2 = player2.player_pos + roll;

    if (new_pos2 <= 100) {
      if (new_pos2 == 100) winner(player2);
      disableButton(1);
      enableButton(2);
      new_pos2 = checkForLadder(new_pos2, player2);
      new_pos2 = checkForSnakes(new_pos2, player2);

      player2.player_pos = new_pos2;
      setPlayerPostion();
    } else {
      turn_counter = 1;
    }
  }
};

document.getElementById("diceButton").onclick = rollDice;
