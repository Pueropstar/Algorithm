/** @format */

const fs = require("fs");

const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

if (N % 2 == 0) {
  console.log("SK");
} else {
  console.log("CY");
}