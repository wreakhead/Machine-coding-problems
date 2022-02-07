export class player {
  constructor() {
    this.name = "";
    this.player_pos = 0;
    this.current_box = "";
    this.prev_box = "";
  }
  check() {
    console.log(this.player_pos, this.current_box, this.prev_box);
  }
}
