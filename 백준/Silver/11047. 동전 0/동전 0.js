const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input.shift().split(" ").map(Number);

const coins = input.map(Number).sort((a, b) => b - a);

let money = K;

let ans = 0;
coins.forEach((el, index) => {
  if (money >= el) {
    ans += Math.floor(money / el);
    money = money % el;
  }
});
console.log(ans);
