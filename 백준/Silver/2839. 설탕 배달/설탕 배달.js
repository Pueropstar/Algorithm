const fs = require("fs");
const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

let remain = N % 5;
let five_quo = Math.floor(N / 5);

let go = 1;

while (go) {
  if (remain % 3 == 0) {
    console.log(five_quo + Math.floor(remain / 3));
    break;
  } else {
    if (five_quo <= 0) {
      console.log(-1);
      break;
    }
    remain += 5;
    five_quo--;
  }
}
