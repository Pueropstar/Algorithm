/** @format */

const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

let last = 0;

input.forEach((data, index) => {
  if (!isNaN(Number(data))){
    last = index;
  }
});

let known_number = Number(input[last]);

let number_ans = known_number + 3 - last;

if (number_ans % 15 == 0) {
  console.log("FizzBuzz");
} else if (number_ans % 3 == 0 && number_ans % 5 != 0) {
  console.log("Fizz");
} else if (number_ans % 3 != 0 && number_ans % 5 == 0) {
  console.log("Buzz");
} else {
  console.log(number_ans);
}
