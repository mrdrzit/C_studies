/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";


let balls = [];

function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

function draw() {
  background(0);
  for (let i = 0; i < balls.length; i++) {
    balls[i].show();
    balls[i].move();
  }
}

function mousePressed(){
  let ball = new Ball(mouseX,mouseY,random(20,45));
  balls.push(ball);
}

class Ball {
  constructor(xpos, ypos, size) {
    this.pos = createVector(xpos, ypos, 200);
    this.speed = p5.Vector.random2D().mult(3);
    this.diameter = size;
    this.color = color(255);
  }

  show() {
    fill(this.color)
    circle(this.pos.x, this.pos.y, this.diameter)
  }

  move() {
    this.pos.add(this.speed);

    if (this.pos.x > width || this.pos.x < 0) {
      this.speed.x = this.speed.x * -1;
      this.color = color(random(20,255), random(50,255), random(80,255));
    }
    else if (this.pos.y > height || this.pos.y < 0) {
      this.speed.y = this.speed.y * -1;
      this.color = color(random(20,255), random(50,255), random(80,255));
    }
  }
}