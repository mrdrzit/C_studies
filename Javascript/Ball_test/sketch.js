/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";


let balls = [];


function setup() {
  createCanvas(400, 400);
  for (let i = 0; i < 1; i++){
    balls[i] = new Ball(random(5,40));
    angleMode(DEGREES);
  }
}

function draw() {
  background(0);
  for (let i = 0; i < balls.length; i++){
    balls[i].show();
    balls[i].move();
  }
}

class Ball {
  constructor(size) {
    this.pos = createVector(200,200)
    this.diameter = size;
    this.speed = 2;
    this.heading = this.pos.heading(random(0,TWO_PI));
  }

  show() {
    circle(this.pos.x, this.pos.y, this.diameter)
  }

  move() {
    this.pos.x = this.pos.x + this.speed;
    if (this.pos.x > width || this.pos.x < 0){
      this.speed = this.speed * -1;
      fill(random(20,255), random(50,255), random(80,255))
    }
  }
}