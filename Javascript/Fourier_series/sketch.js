/// <reference path="TSDef/p5.global-mode.d.ts" />
"use strict";


// Fórmula >>> y(t) = Asin(2PI * f * t + PHI)

let Fs = 2000;    // Amostragem
let dt = 1 / Fs;    // seconds per sample
let Time = 3;     // seconds
let timeVector = (math.range(0, Time, dt));
let wave;
let wave2;
let wavesum;
function setup() {
  
  createCanvas(600, 600);
  wave = createWave(6, 10, timeVector);
  wave2 = createWave(12, 20, timeVector);
  wavesum = math.add(wave,wave2);
}

function draw() {
  translate(width/100, height/2)
  background(0, 22, 30);
  drawSw(wave, timeVector);
  translate(width/4000, height/12);
  drawSw(wave2, timeVector);
  translate(width/3500, height/12);
  drawSw(wavesum, timeVector);

}

function createWave(A, F, T, phase = 0) {
  let dataY = [];
  for (let i = 0; i < T._data.length; i++) {
    let y = A * sin(TWO_PI * F * T._data[i] + phase)
    dataY.push(y);
  }
  return dataY
}

function drawSw(xValues, yValues) {
  for (let i = 0; i < wave.length; i++) {
    noStroke();
    fill(255);
    circle(i,xValues[i],2);
  }
}