/** @format */

let inputString = require("fs").readFileSync("/dev/stdin").toString().trim();

const input = Number(inputString);

let index = 0;
let num = 0;

let arr = []
while (1) {
  
  if (num.toString().includes('666')){
    arr.push(num);
    index++;
  }
  if (arr.length == input){
    break;
  }
  num++;
}

console.log(arr[index-1]);
