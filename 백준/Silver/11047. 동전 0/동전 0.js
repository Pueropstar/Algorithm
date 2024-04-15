const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input[0].split(" ").map(Number);

const valueArr = [];

let target = K;

let ans = 0;

for (let i = 1; i <= N; i++) {
  const value = Number(input[i]);
  valueArr.push(value);
}

valueArr.forEach((el, index) => {
  if (valueArr[N - 1 - index] <= target) {
    while (valueArr[N - 1 - index] <= target) {
      target -= valueArr[N - 1 - index];
      ans++;
    }
  }
});

console.log(ans);