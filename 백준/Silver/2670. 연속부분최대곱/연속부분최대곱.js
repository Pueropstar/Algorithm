/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

let temp = Number(input[1]);

let ans = 0;

for (let i = 2; i <= N; i++) {
  let num = Number(input[i]);
  if (num > num * temp) {
    temp = num;
  } else {
    temp *= num;
  }
  ans = Math.max(ans, temp);
}
console.log(ans.toFixed(3));