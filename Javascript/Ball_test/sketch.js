/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";

var gravity = 1;
var y = 0;

function setup(){
  createCanvas(400, 400);
}

function draw(){
  background(100);
  fill(210,120,22);
  noStroke();
  ellipseMode(CENTER);
  ellipse(width/2, y, 30);

  if (y > height || y < 0){
    gravity = gravity * -1;
  }
  y = y + gravity
}

class ball{
  constructor(){
    this.x = width/2;
    this.y = height/2;
    let velocity = 0;
  }
}