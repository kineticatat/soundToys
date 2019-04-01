// Run this example on a mobile device
// Rotate the device by 90 degrees in the
// X-axis to change the value.

var value = 0;
function draw() {
  fill(value);
  rect(25, 25, 50, 50);
}
function deviceTurned() {
  if (turnAxis === 'X') {
    if (value === 0) {
      value = 255;
    } else if (value === 255) {
      value = 0;
    }
  }
}
