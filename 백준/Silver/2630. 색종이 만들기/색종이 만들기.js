const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const confetti = [];

// 0은 0 1은 1
let ans = Array(2).fill(0);

for (let i = 0; i < N; i++) {
  confetti.push(input[1 + i].split(" ").map(Number));
}

const divideConquer = (row, col, size) => {
  if (check(row, col, size)) {
    const num = confetti[row][col];

    switch (num) {
      case 0:
        ans[0]++;
        break;
      case 1:
        ans[1]++;
        break;
    }
  } else {
    let divided_size = size / 2;
    for (let i = 0; i < 2; i++) {
      for (let j = 0; j < 2; j++) {
        divideConquer(
          row + i * divided_size,
          col + j * divided_size,
          divided_size
        );
      }
    }
  }
};

const check = (row, col, size) => {
  const target = confetti[row][col];

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (confetti[i + row][j + col] !== target) {
        return false;
      }
    }
  }
  return true;
};

divideConquer(0, 0, N);

for (const num of ans) {
  console.log(num);
}