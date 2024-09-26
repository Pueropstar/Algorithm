const fs = require("fs");
const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const T = Number(input.shift());
const cases = input.map(Number);

let zero_arr = [1, 0];
let one_arr = [0, 1];

let max = Math.max(...cases);

for (let i = 2; i <= max; i++) {
  zero_arr[i] = zero_arr[i - 2] + zero_arr[i - 1];
  one_arr[i] = one_arr[i - 2] + one_arr[i - 1];
}

cases.forEach((data) => {
  console.log(zero_arr[data], one_arr[data]);
});
