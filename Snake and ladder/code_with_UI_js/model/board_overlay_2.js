let blocks = "";

let odd_blocks = 100;
let even_blocks = 81;

const generateRowId = (x) => {
  return "id='row" + x + "'";
};

const generateBoxId = (x) => {
  return "id='boxTwo" + x + "'";
};

for (let i = 1; i <= 10; i++) {
  let newDiv = "<div class='rows' " + generateRowId(i) + ">";
  if (i % 2 != 0) {
    for (let k = odd_blocks; k >= odd_blocks - 9; k--) {
      newDiv += "<div class='boxTwo'" + generateBoxId(k) + "></div>";
    }
    odd_blocks = odd_blocks - 20;
  } else {
    for (let k = even_blocks; k <= even_blocks + 9; k++) {
      newDiv += "<div class='boxTwo'" + generateBoxId(k) + "></div>";
    }
    even_blocks = even_blocks - 20;
  }
  newDiv += "</div>";

  blocks += newDiv;
}

document.getElementById("blocks2").innerHTML = blocks;
