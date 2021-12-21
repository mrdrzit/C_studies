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
  for (let i = 0; i < balls.length; i++) {
    balls[i].show();
    balls[i].move();
    let lamp = false;
    for (let j = i; j < balls.length; j++) {
      if (ball !== balls[i] && balls[i].isOverlapping(elem)) {
        lamp = true;
      }
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