const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [K, N] = input.shift().split(" ").map(Number);
const cables = input.map(Number).sort((a, b) => a - b);

let start = 0;
let end = cables[cables.length - 1];

while (start <= end) {
  let mid = Math.floor((start + end) / 2); // 내림
  
  let lineNum = cables.reduce((acc, cur) => acc + Math.floor(cur / mid), 0);
  // Q. Math.floor VS parsInt : Math.floor 연산이 더 빠르다고 한다. 이거때문에 처음에 틀렸나...? 뭐지 ㅠ

  if (lineNum >= N) {
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(end); // 목표인 N 개의 랜선을 만들 수 있는 경우에서, end는 가장 큰 값이 보장됨 (start 부분을 늘리기 때문)