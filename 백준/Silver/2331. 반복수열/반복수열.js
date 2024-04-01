const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

function solve(start) {
  const queue = [start];
  checked.push(start);

  while (queue.length !== 0) {
    let sum = 0;
    v = queue.shift();

    for (let i = 0; i < v.length; i++) {
      sum += Number(v[i]) ** P;
    }
    const sumString = sum.toString();
    if (!checked.includes(sumString)) {
      queue.push(sumString);
      checked.push(sumString);
    } else {
      const ans = checked.indexOf(sumString);
      console.log(ans);
    }
  }
}
const [A, P] = input[0].split(" ");

const checked = [];

solve(A);