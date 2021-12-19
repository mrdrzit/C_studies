/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";

let ball;

function setup() {
  createCanvas(400, 400);
  ball = new Ball(30);
}

function draw() {
  background(0);
  ball.show();
  ball.move();
}

class Ball {
  constructor(size) {
    this.x = 200;
    this.y = 200;
    this.diameter = size;
    this.speed = 2;
  }

  show() {
    circle(this.x, this.y, this.diameter)
  }

  move() {
    this.x = this.x + this.speed;
    if (this.x > width || this.x < 0){
      this.speed = this.speed * -1;
      fill(random(20,255), random(50,255), random(80,255))
    }
  }
}