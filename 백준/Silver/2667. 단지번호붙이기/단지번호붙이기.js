const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const graph = Array.from({ length: N }, () => []);

const result = [];

let apartment = 0;

for (let i = 0; i < N; i++) {
  graph[i] = input[i + 1].trim().split("").map(Number);
}
// 상 하 좌 우
const bfs = (y, x) => {
  let count = 1;
  const queue = [{ y, x }];
  const dy = [-1, 1, 0, 0];
  const dx = [0, 0, -1, 1];

  graph[y][x] = 0;

  while (queue.length !== 0) {
    const { y, x } = queue.shift();
    for (let i = 0; i < dy.length; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (0 <= ny && ny < N && 0 <= nx && nx < N && graph[ny][nx] == 1) {
        queue.push({ y: ny, x: nx });
        graph[ny][nx] = 0;
        count++;
      }
    }
  }
  result.push(count);
};

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (graph[i][j] == 1) {
      bfs(i, j);
      apartment++;
    }
  }
}
console.log(apartment);
[
  ...result.sort(function (a, b) {
    return a - b;
  }),
].forEach((el) => console.log(el));
