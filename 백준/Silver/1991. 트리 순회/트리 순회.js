const fs = require("fs");
const input = fs
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const N = input[0];

const tree = Array.from({ length: N + 1 }, () => []);

let preAns = "",
  inAns = "",
  postAns = "";

for (let i = 0; i < N; i++) {
  const [node, left, right] = input[1 + i].trim().split(" ");
  tree[node] = [left, right];
}

const preOrder = (node) => {
  if (node === ".") return;

  const [left, right] = tree[node];

  preAns += node;
  preOrder(left);
  preOrder(right);
};
const inOrder = (node) => {
  if (node === ".") return;

  const [left, right] = tree[node];

  inOrder(left);
  inAns += node;
  inOrder(right);
};
const postOrder = (node) => {
  if (node === ".") return;

  const [left, right] = tree[node];

  postOrder(left);
  postOrder(right);
  postAns += node;
};

preOrder("A");
console.log(preAns);
inOrder("A");
console.log(inAns);
postOrder("A");
console.log(postAns);