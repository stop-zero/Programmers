function solution(s) {
    var answer = 0;
    const arr = s.split(' ');
    for(let i=0; i<arr.length; i++){
        const item = (arr[i]);
        if(item !== 'Z'){
            answer += Number(item);
        }else{
            answer -= Number(arr[i-1])
        }
    }
    return answer;
}