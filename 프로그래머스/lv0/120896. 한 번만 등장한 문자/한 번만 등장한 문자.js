function solution(s) {
    let list = s.split('').sort();
    let answer = [];
    while(list.length) {
        let target = list.shift()
        if(list[0] == target) {
            while(list[0] == target) {
                list.shift();
            }
        } else {
            answer.push(target);
        }
    }
    return answer.join('');
}