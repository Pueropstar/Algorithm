const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");
const bfs = (start) => {
  let count = 1;
  const queue = [start];
  visited[start] = count;

  while (queue.length !== 0) {
    const v = queue.shift();

    for (const i of graph[v]) {
      if (!visited[i]) {
        queue.push(i);
        visited[i] = ++count;
      }
    }
  }
};
const [N, M, R] = input[0].split(" ").map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array(N + 1).fill(0);

for (let i = 1; i <= M; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}
graph.map((line) => line.sort((a, b) => a - b));

bfs(R);

console.log(visited.slice(1).join("\n"));