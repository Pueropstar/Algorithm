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

let first = BigInt(0);
let second = BigInt(1);

let dp = [first, second];

for (let i = 2; i <= N; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
}

if (N == 1) {
  console.log(4);
} else {
  console.log((dp[N] * BigInt(2) + (dp[N] + dp[N - 1]) * BigInt(2)).toString());
}