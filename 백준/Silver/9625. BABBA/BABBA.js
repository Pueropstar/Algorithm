/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const K = Number(input[0]);

const regxA = /A/g;
const regxB = /B/g;

const dp = [
  [1, 0],
  [0, 1],
];

for (let i = 2; i <= K; i++) {
  dp[i] = [dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]];
}

console.log(dp[K][0], dp[K][1]);