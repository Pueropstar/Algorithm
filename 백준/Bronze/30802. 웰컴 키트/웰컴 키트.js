/** @format */

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const size_arr = input[1].split(" ").map(Number);

const [T, P] = input[2].split(" ").map(Number);

let t_ans = 0;
let bundle = Math.floor(N / P);
let piece = N % P;

size_arr.forEach((data) => {
  if (data == 0) {
    return;
  } else if (data < T) {
    t_ans++;
  } else if (data % T == 0) {
    t_ans += Math.floor(data / T);
  } else {
    t_ans += Math.floor(data / T) + 1;
  }
});

console.log(t_ans);
console.log(bundle, piece);