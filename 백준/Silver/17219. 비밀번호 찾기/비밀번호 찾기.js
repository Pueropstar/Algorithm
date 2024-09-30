const fs = require("fs");
const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const ans = {};

for (let i = 1; i <= N; i++) {
  const [url, pw] = input[i].split(" ");
  ans[url] = pw.trim();
}

for (let i = N + 1; i <= N + M; i++) {
  console.log(ans[input[i].trim()]);
}