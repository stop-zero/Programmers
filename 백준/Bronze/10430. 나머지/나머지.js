// 파일을 읽어오기 위해 Node.js의 built-in file system module fs 사용
const fs = require("fs");

//input을 읽어와 변수로 선언 & 할당
// 그 내용을 input에 저장, toString(), split()을 사용해서 Array로 저장
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("/n");

// input 가공부분
input = input
  .toString()
  .split(" ")
  .map((v) => Number(v));
//console.log(input); // input 값 확인용

let output = sloution(input[0],input[1],input[2]); // solution에 파라미터 넣어주기

///////////////////////////////////////////////////////////////
// 문제 로직 구현

function sloution(a, b, c) {
  console.log((a + b) % c); //출력값
  console.log(((a % c) + (b % c)) % c);
  console.log((a * b) % c);
  console.log(((a % c) * (b % c)) % c);
  /* let answer;
  answer = input - 543;
  return answer; */
}
