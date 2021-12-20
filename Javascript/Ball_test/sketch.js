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

// function mousePressed(){
//   let ball = new Ball(random(30,50));
//   balls.push(ball);
// }

class Ball {
  constructor(size) {
    this.pos = createVector(200,200)
    this.speed = createVector(4,1)
    this.diameter = size;
  }

  show() {
    circle(this.pos.x, this.pos.y, this.diameter)
  }

  move() {
    this.pos.add(this.speed);
    
    if (this.pos.x > width || this.pos.x < 0){
      this.speed.x = this.speed.x * -1;
      fill(random(20,255), random(50,255), random(80,255))
    }
    else if (this.pos.y > height || this.pos.y < 0){
      this.speed.y = this.speed.y * -1;
      fill(random(20,255), random(50,255), random(80,255))
    }
  }
}