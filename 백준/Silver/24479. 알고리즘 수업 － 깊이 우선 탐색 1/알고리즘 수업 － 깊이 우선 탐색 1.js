const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const dfs = (start, count) => {
  const queue = [start];
  visited[start] = count;
  while (queue.length !== 0) {
    v = queue.pop();

    if (graph[v]) {
      for (const next of graph[v]) {
        if (!visited[next]) {
          count = dfs(next, ++count);
        }
      }
    }
  }
  return count;
};
const [N, M, R] = input[0].split(" ").map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array.from({ length: N + 1 }, () => 0);

let count = 1;
for (let i = 0; i < M; i++) {
  const [u, v] = input[1 + i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

graph.map((line) => line.sort((a, b) => a - b));

dfs(R, count);

console.log(visited.slice(1).join("\n"));