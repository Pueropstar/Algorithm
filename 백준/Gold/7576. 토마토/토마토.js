const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

class Node {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class Deque {
  constructor(value) {
    this.init();
  }
  init() {
    this.count = 0;
    this.head = null;
    this.tail = null;
  }
  shift() {
    if (this.count === 0) return null;

    const value = this.head.value;

    if (this.count === 1) {
      this.init();
    } else {
      this.head = this.head.next;
      this.head.prev = null;
      this.count--;
    }
    return value;
  }
  push(value) {
    const node = new Node(value);

    if (this.count === 0) {
      this.head = node;
      this.tail = node;
    } else {
      const prevNode = this.tail;
      prevNode.next = node;
      node.prev = prevNode;
      this.tail = node;
    }
    this.count++;
  }
}

const [M, N] = input[0].split(" ").map(Number);

const graph = Array.from({ length: N }, () => []);

const queue = new Deque();

let ans = 0;

for (let i = 0; i < N; i++) {
  graph[i] = input[1 + i].split(" ").map(Number);
}

// 상 하 좌 우

const bfs = (queue, hostCount) => {
  const dy = [-1, 1, 0, 0];
  const dx = [0, 0, -1, 1];
  let flag = 0;
  let count = 0;
  while (queue.count !== 0) {
    const [y, x] = queue.shift();

    for (let i = 0; i < dy.length; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];

      if (0 <= ny && ny < N && 0 <= nx && nx < M && graph[ny][nx] == 0) {
        if (hostCount > 0) {
          graph[ny][nx] = graph[y][x];
        } else {
          graph[ny][nx] = graph[y][x] + 1;
        }
        queue.push([ny, nx]);
        count = Math.max(ans, graph[ny][nx]);
      }
    }
    hostCount--;
  }
  return count;
};

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (graph[i][j] == 1) {
      queue.push([i, j]);
    }
  }
}
const hostCount = queue.count;

ans = bfs(queue, hostCount);

for (const arr of graph) {
  if (arr.includes(0)) {
    ans = -1;
    break;
  }
}

console.log(ans);