class Ball {
  constructor(size, color = 120) {
    this.pos = createVector(random(90, height - 100), random(80, height - 100));
    this.speed = p5.Vector.random2D().mult(3);
    this.diameter = size;
    this.color = color;
  }

  isOverlapping(object) {
    let d = dist(this.pos.x, this.pos.y, object.pos.x, object.pos.y);
    if (d < this.diameter / 2 + object.diameter / 2) {
      return true;
    } else {
      return false;
    }
  }

  changeColor(lambda) {
    this.color = lambda;
  }

  isInside(xpos, ypos) {
    if (dist(xpos, ypos, this.pos.x, this.pos.y) > this.diameter / 2) {
      return false;
    } else {
      return true;
    }
  }

  show() {
    fill(this.color)
    circle(this.pos.x, this.pos.y, this.diameter)
  }

  move() {
    let r = this.diameter / 2;
    this.pos.add(this.speed);

    if (this.pos.x + r > width || this.pos.x < 0 + r) {
      this.speed.x = this.speed.x * -1;
    }
    else if (this.pos.y + r > height || this.pos.y < 0 + r) {
      this.speed.y = this.speed.y * -1;
    }
  }
}