/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const Numbers = input[1].split(" ").map(Number);

let asc_combo = Array.from({ length: N }, () => 1);
let des_combo = Array.from({ length: N }, () => 1);

for (let i = 1; i < N; i++) {
  if (Numbers[i - 1] <= Numbers[i]) {
    asc_combo[i] = asc_combo[i - 1] + 1;
  }
  if (Numbers[i - 1] >= Numbers[i]) {
    des_combo[i] = des_combo[i - 1] + 1;
  }
}
console.log(Math.max(...asc_combo, ...des_combo));