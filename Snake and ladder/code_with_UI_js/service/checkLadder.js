import { ladders } from "../model/ladders.js";
import { triggerModal } from "./triggerModal.js";

export const checkForLadder = (pos, player) => {
  if (ladders.get(pos) !== undefined) {
    const message = player.name + " Got ladder at " + pos;
    console.log(message);
    triggerModal(message);
    return ladders.get(pos);
  } else {
    return pos;
  }
};
