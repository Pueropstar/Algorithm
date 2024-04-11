const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const dfs = (start) => {
  stack.push(start);
  visited[start] = true;

  while (stack.length !== 0) {
    const v = stack.pop();

    if (tree[v]) {
      for (const next of tree[v]) {
        if (!visited[next]) {
          ans[next] = v;
          dfs(next);
        }
      }
    }
  }
};
const N = Number(input[0]);

const tree = Array.from({ length: N + 1 }, () => []);

const ans = Array.from({ length: N + 1 }, () => []);

const visited = Array.from({ length: N + 1 }, () => false);

const stack = [];

for (let i = 0; i < N - 1; i++) {
  const [u, v] = input[1 + i].split(" ").map(Number);
  tree[u].push(v);
  tree[v].push(u);
}

dfs(1);

console.log(ans.slice(2).join("\n"));