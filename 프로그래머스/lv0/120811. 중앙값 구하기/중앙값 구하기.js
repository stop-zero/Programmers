function solution(array) {
    let Array_Input = array.sort(function(a, b) { 
    return a - b});
  
    return Array_Input[parseInt(array.length/2)];
}