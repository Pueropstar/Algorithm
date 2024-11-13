/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);

let graph = [];
let queue = [];
let graph_distance = Array.from({ length: N }, () => Array(M).fill(0));

let start_x = 0;
let start_y = 0;

const bfs = (input_y, input_x) => {
  queue.push([input_y, input_x]);
  const dy = [-1, 1, 0, 0];
  const dx = [0, 0, -1, 1];

  while (queue.length !== 0) {
    const [y, x] = queue.shift();

    for (let i = 0; i < dy.length; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];

      if (0 <= ny && ny < N && 0 <= nx && nx < M && graph[ny][nx] == 1) {
        graph_distance[ny][nx] = graph_distance[y][x] + 1;
        graph[ny][nx] = -1;
        queue.push([ny, nx]);
      }
    }
  }
};

for (let i = 0; i < N; i++) {
  graph.push(input[1 + i].split(" ").map(Number));
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (graph[i][j] == 2) {
      start_y = i;
      start_x = j;
    }
  }
}
bfs(start_y, start_x);

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (graph[i][j] == 1) {
      graph_distance[i][j] = -1;
    }
  }
}

let ans = "";
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    ans += graph_distance[i][j] + " ";
  }
  ans += "\n";
}
console.log(ans)