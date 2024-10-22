/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);

const arr = input[1].split(" ").map(Number);

let sum_arr = [arr[0]];

let ans_arr = [];

for (let i = 1; i < N; i++) {
  sum_arr[i] = sum_arr[i - 1] + arr[i];
}

for (let i = 0; i < M; i++) {
  const [start, end] = input[2 + i].split(" ").map(Number);

  if (start > 1) {
    ans_arr.push(sum_arr[end - 1] - sum_arr[start - 2]);
  } else {
    ans_arr.push(sum_arr[end - 1]);
  }
}

console.log(ans_arr.join("\n"));
