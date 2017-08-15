var rad = 10;
var backColor = 0;

function setup() {
    createCanvas(windowWidth, windowHeight);
}

function draw() {
    background(backColor);
    fill(255);
    translate(windowWidth / 2, windowHeight / 2);
    noStroke();
    ellipse(0, 0, rad, rad);
    rad += 20;
    backColor += 3;
}
