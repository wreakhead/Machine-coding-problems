import { snakes } from "../model/snakes.js";
import { triggerModal } from "./triggerModal.js";

export const checkForSnakes = (pos, player) => {
  if (snakes.get(pos) !== undefined) {
    const message = player.name + " Got Bitten at " + pos;
    console.log(message);
    triggerModal(message);
    return snakes.get(pos);
  } else {
    return pos;
  }
};
