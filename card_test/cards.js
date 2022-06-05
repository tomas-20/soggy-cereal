const ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
const suites = ["C", "D", "H", "S"];
const cards = {};

function getImage(path) {
  const image = new Image();
  image.src = path;
  return image;
}

for (const rank of ranks) {
  for (const suite of suites) {
    const card = rank + suite;
    cards[card] = getImage("card_svgs/" + card + ".svg");
  }
}

function drawImage(context, image, x, y, height) {
  context.drawImage(image, x, y, image.width * height / image.height, height);
}

function drawCard(context, card, x, y, height) {
  drawImage(context, cards[card], x, y, height);
}