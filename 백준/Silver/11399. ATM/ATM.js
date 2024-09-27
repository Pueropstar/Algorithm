const fs = require("fs");
const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const times = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const time_sum = [times[0]];

for (let i = 1; i < N; i++) {
  time_sum[i] = times[i] + time_sum[i - 1];
}

const ans = time_sum.reduce((acc, num) => acc + num, 0);

console.log(ans);