/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";


let balls = [];

function setup() {
  createCanvas(400, 400);
  for (let i = 0; i < 10; i++) {
    let ball = new Ball(50);
    balls.push(ball);
  }
}

function draw() {
  background(0);
  
  for (let ball of balls) {
    ball.show();
    ball.move();
    let lamp = false;
    for (let elem of balls){
      if (ball !== elem && ball.isOverlapping(elem)) {
        lamp = true;
      }
    }
    if (lamp){
      ball.changeColor(200);
    } else {
      ball.changeColor(40);
    }
  }
}

function mousePressed() {
  for (let i = 0; i < balls.length; i++) {
    if (balls[i].isInside(mouseX, mouseY) && mouseButton === CENTER) {
      balls.splice(i, 1);
    }
  }
}
