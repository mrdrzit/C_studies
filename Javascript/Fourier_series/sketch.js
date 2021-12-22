/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";


// Fórmula >>> y(t) = Asin(2PI * f * t + PHI)
let frequency = 2;
let time = 60;
let angle = 0;
let amplitude = 1;
let valuesY = [];
let timeVector = [];
let posVector = [];


function setup() {
  createCanvas(600, 600);
  angleMode(RADIANS);
}

function draw() {
  background(0,22,30);
  createWave(amplitude, frequency, time)
  drawSw(valuesY, timeVector)
}

function createWave(A, F, T, phase = 0){

  for (let itempo = 0; itempo < T; itempo++){
    let y = A * sin(TWO_PI * F * itempo)
    valuesY.push(y);
    timeVector[itempo] = itempo;
  }
}

function drawSw(yValues, xValues){
  for (let pos = 0; pos < xValues.length; pos++) {
    posVector.push(pos);
  }
  for(let i = 0; i < yValues; i++){
    point(posVector[i], yValues[i])
    strokeWeight(10)
  }
}