function solution(n) {
  let cnt = 0;
  let factorial = 1;
  let num = 0;
  while (factorial <= n) {
      num++;
      factorial *= num;
  }
  return num - 1;
}