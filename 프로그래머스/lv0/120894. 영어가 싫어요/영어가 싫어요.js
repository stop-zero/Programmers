function solution(numbers) {
     let obj = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ];

    obj.forEach((str, idx) => {
        numbers = numbers.replaceAll(str, idx);
    });
    return Number(numbers);
}