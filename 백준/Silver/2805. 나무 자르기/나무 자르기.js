/** @format */

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

//N 은 나무의 수 M은 남겨야 할 길이
const [N, M] = input[0].split(" ").map(Number);

const trees = input[1].split(" ").map(Number);

let start = 0;
let end = Math.max(...trees);

while (start <= end) {
  let mid = Math.floor((start + end) / 2);

  let sum_cut = 0;

  trees.forEach((data) => {
    let result = data - mid;
    if (result >= 0) {
      sum_cut += data - mid;
    }
  });

  if (sum_cut >= M) {
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(end);