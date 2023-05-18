function solution(order) {
    var answer = 0;
   let orders = order.toString().split('');
    
    for(let order of orders){
        if(order ==='3' || order === '6' || order === '9'){
            answer++
        }
    }
    return answer;
}