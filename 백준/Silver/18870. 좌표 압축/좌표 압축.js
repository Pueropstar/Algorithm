/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const pos_arr = input[1].split(" ").map(Number);
const sorted_arr = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const obj = {};

let ans = "";

let compress = 0;

for (let i = 0; i < N; i++) {
  if (obj[sorted_arr[i]] == undefined) {
    obj[sorted_arr[i]] = compress;
    compress++;
  }
}
for (const element of pos_arr) {
  ans = ans + obj[element] + " ";
}
console.log(ans);