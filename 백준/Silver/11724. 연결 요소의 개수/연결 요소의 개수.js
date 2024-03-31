const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function solution(arr) {
  function bfs(start) {
    visited[start] = true;
    const queue = [start];
    while (queue.length !== 0) {
      const v = queue.shift();
      graph[v].forEach((el) => {
        if (!visited[el]) {
          visited[el] = true;
          queue.push(el);
        }
      });
    }
  }

  const [N, M] = arr[0].split(" ").map(Number);

  const graph = Array.from({ length: N + 1 }, () => []);
  const visited = Array.from({ length: N + 1 }, () => false);

  let ans = 0;

  for (let i = 0; i < M; i++) {
    const [u, v] = input[i + 1].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      bfs(i);
      ans++;
    }
  }
  return ans;
}

console.log(solution(input));
