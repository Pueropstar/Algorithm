const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

function bfs(start) {
  const queue = [start];
  visited[start] = true;

  while (queue.length !== 0) {
    const v = queue.shift();

    if (graph[v]) {
      graph[v].forEach((el) => {
        if (!visited[el]) {
          queue.push(el);
          visited[el] = true;
        }
      });
    }
  }
}

const T = Number(input[0]);

for (let i = 0; i < T; i++) {
  const N = Number(input[(i*2) + 1]);

  const arr = input[(i*2) + 2].split(" ").map(Number);

  var visited = Array.from({ length: N + 1 }, () => false);

  var graph = Array.from({ length: N + 1 }, () => []);

  let ans = 0;

  for (let j = 0; j < N; j++) {
    graph[j + 1].push(arr[j]);
  }
  
  for (let j = 1; j <= N; j++) {
    if (!visited[j]) {
      bfs(j);
      ans++;
    }
  }
  console.log(ans);
}
