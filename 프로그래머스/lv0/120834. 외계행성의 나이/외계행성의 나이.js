function solution(age) {
    const ageArr = String(age).split("");
    
    let answer = "";
    
    for(let i = 0; i < ageArr.length; i++){
        answer += String.fromCharCode(Number(ageArr[i]) + 97);
    }
    
    return answer;
}
