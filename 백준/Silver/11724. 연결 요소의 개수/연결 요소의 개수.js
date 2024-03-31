const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function solution(arr) {
  function bfs(start) {
    visited[start] = true;
    const queue = [start];
    while (queue.length !== 0) {
      const v = queue.shift();

      if (graph[v]) {
        graph[v].forEach((data, index) => {
          if (!visited[data]) {
            visited[data] = true;
            queue.push(data);
          }
        });
      }
    }
  }

  const [N, M] = arr[0].split(" ").map(Number);

  const graph = new Array(N+1).fill().map(() => []);

  const visited = new Array(N+1).fill(false);

  let ans = 0;

  for (let i = 0; i < M; i++) {
    const [u, v] = input[i + 1].split(" ").map(Number);
    if (graph[u]) graph[u].push(v);
    if (graph[v]) graph[v].push(u);
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
