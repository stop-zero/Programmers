function solution(numbers) {
    var answer = 0;
    var n = 0;
    numbers.sort((a,b)=>a-b);
    n=numbers.length;
    answer = numbers[n-1]*numbers[n-2];
    return answer;
}