const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const confetti = [];

for (let i = 0; i < N; i++) {
  confetti.push(input[1 + i].split(" ").map(Number));
}

// -1 0 1
let result = Array(3).fill(0);

const divideConquer = (row, col, size) => {
  if (check(row, col, size)) {
    const num = confetti[row][col];

    switch (num) {
      case -1:
        result[0]++;
        break;
      case 0:
        result[1]++;
        break;
      case 1:
        result[2]++;
        break;
    }
  } else {
    const divided = size / 3;

    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        divideConquer(row + i * divided, col + j * divided, divided);
      }
    }
  }
};

const check = (row, col, size) => {
  const target = confetti[row][col];

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (confetti[row + i][col + j] !== target) {
        return false;
      }
    }
  }

  return true;
};

divideConquer(0, 0, N);

for (const ans of result) {
  console.log(ans);
}