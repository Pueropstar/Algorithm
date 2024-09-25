const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [K, N] = input.shift().split(" ").map(Number);
const sorted_arr = input.map(Number).sort((a, b) => a - b);


let start = 0;

let end = sorted_arr[sorted_arr.length - 1];

while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  
  let sum_quo = sorted_arr.reduce(
    (acc, data) => acc + Math.floor(data / mid),
    0
  );

  if (sum_quo >= N) {
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(end);