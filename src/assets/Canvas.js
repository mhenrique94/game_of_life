class Canvas {
  constructor(w, h, border) {
    this.canvas = document.getElementById("GOLCanvas");
    if (!this.canvas) this.createcanvas(border, w, h);
    if (w) this.canvas.width = w;
    if (h) this.canvas.height = h;
    this.ctx = this.canvas.getContext("2d");
    this.width = this.ctx.canvas.clientWidth;
    this.height = this.ctx.canvas.clientHeight;
    this.canvas.addEventListener("mousemove", (e) => {
      this.mousemove(e);
    });
    this.canvas.addEventListener("click", (e) => {
      this.mouseclick(e);
    });
  }
  rectangle(x, y, width, height, bordercolor, fillcolor, opacity, weight) {
    this.setColor(bordercolor, fillcolor, opacity);
    this.ctx.lineWidth = weight || 1;
    if (fillcolor) this.ctx.fillRect(x, y, width, height);
    if (bordercolor) this.ctx.strokeRect(x, y, width, height);
  }

  mousemove(e) {
    if (this.OnMouseMove) this.OnMouseMove(e);
  }
  mouseclick(e) {
    if (this.OnMouseClick) this.OnMouseClick(e);
  }
  createcanvas(border, w, h) {
    this.canvas = document.createElement("canvas");
    this.canvas.style.border = border || "1px solid";
    this.canvas.width = w || window.innerWidth - 30;
    this.canvas.height = h || window.innerHeight - 30;
    var body = document.getElementsByTagName("body")[0];
    body.appendChild(this.canvas);
  }
  setColor(bordercolor, fillcolor, opacity) {
    this.ctx.globalAlpha = opacity || 1;
    this.ctx.strokeStyle = bordercolor;
    this.ctx.fillStyle = fillcolor;
  }

  point(x, y, color, width, opacity) {
    this.setColor(color || "black", color || "black", opacity);
    width = width || 1;
    let m = width / 2;
    this.ctx.fillRect(x - m, y - m, width, width);
  }
  circle(x, y, r, bordercolor, fillcolor, opacity) {
    this.setColor(bordercolor, fillcolor, opacity);
    this.ctx.beginPath();
    this.ctx.arc(x, y, r, 0, 2 * Math.PI);
    this.ctx.closePath();
    if (fillcolor) this.ctx.fill();
    if (bordercolor) this.ctx.stroke();
  }
  line(x1, y1, x2, y2, color, opacity) {
    this.setColor(color, color, opacity);
    this.ctx.beginPath();
    this.ctx.moveTo(x1, y1);
    this.ctx.lineTo(x2, y2);
    this.ctx.stroke();
  }
  center(x, y) {
    this.ctx.translate(x, y);
  }
  save() {
    this.ctx.save();
  }
  restore() {
    this.ctx.restore();
  }
  rotate(radians) {
    this.ctx.rotate(radians);
  }
  clear(color, opacity) {
    if (color)
      this.rectangle(0, 0, this.width, this.height, color, color, opacity);
    else this.ctx.clearRect(0, 0, this.width, this.height);
  }
  curve(x1, y1, x2, y2, refx, refy, color, opacity) {
    this.setColor(color, color, opacity);
    this.ctx.beginPath();
    this.ctx.moveTo(x1, y1);
    refx *= 0.95;
    refy *= 0.95;
    this.ctx.quadraticCurveTo(refx, refy, x2, y2);
    this.ctx.stroke();
  }
}

export default Canvas;
