const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);

const graph = Array.from({ length: N }, () => []);

for (let i = 0; i < N; i++) {
  graph[i] = input[1 + i].trim().split("").map(Number);
}

// 상 하 좌 우
const bfs = (y, x) => {
  const queue = [{ y, x }];

  const dy = [-1, 1, 0, 0];
  const dx = [0, 0, -1, 1];

  while (queue.length !== 0) {
    const { y, x } = queue.shift();
    for (let i = 0; i < dy.length; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (0 <= ny && ny < N && 0 <= nx && nx < M && graph[ny][nx] === 1) {
        graph[ny][nx] = graph[y][x] + 1;
        queue.push({ y: ny, x: nx });
      }
    }
  }
  console.log(graph[N - 1][M - 1]);
};

bfs(0, 0);
