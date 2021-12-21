class Ball {
    constructor(size) {
        this.pos = createVector(random(20, height - 20), random(20, height - 20));
        this.speed = p5.Vector.random2D().mult(2);
        this.diameter = size;
        this.color = color(255);
    }

    show() {
        fill(this.color)
        circle(this.pos.x, this.pos.y, this.diameter)
    }

    isInside(xpos, ypos) {
        if (dist(xpos, ypos, this.pos.x, this.pos.y) > this.diameter / 2) {
            return false;
        } else {
            return true;
        }
    }

    move() {
        this.pos.add(this.speed);

        if (this.pos.x > width || this.pos.x < 0) {
            this.speed.x = this.speed.x * -1;
            this.color = color(random(20, 255), random(50, 255), random(80, 255));
        }
        else if (this.pos.y > height || this.pos.y < 0) {
            this.speed.y = this.speed.y * -1;
            this.color = color(random(20, 255), random(50, 255), random(80, 255));
        }
    }
}