function solution(my_string) {
    return my_string.replaceAll(/[^\d]/g, '').split('').map(n=>+n).reduce((a,n)=>a+n,0);
}