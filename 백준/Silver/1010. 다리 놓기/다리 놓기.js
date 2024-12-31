const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const T = Number(input[0]);

const facto = (num) => {
  if (num == 0) {
    return 1;
  }

  return num * facto(num - 1);
};

for (let i = 0; i < T; i++) {
  const [r, n] = input[1 + i].split(" ").map(Number);

  console.log(Math.round(facto(n) / (facto(r) * facto(n - r))));
}