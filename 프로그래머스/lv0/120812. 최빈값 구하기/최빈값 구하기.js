

  function solution(array) {
      let srtArray = array.sort((a, b) => a-b);
    let a = 0; 
    let i = -1;
    let aRepeat = 0;
    let iRepeat = 0;
    let beforeNum = -1;
    let Double = false;



    while( a < array.length){

        if(beforeNum !== array[a]){
            aRepeat = 1;
        } else{
            aRepeat = aRepeat + 1;
        }

        if(iRepeat === aRepeat){
            if(i !== array[a]){
                Double = true;
            }
        }
        if(aRepeat > iRepeat){
            i = array[a];
            iRepeat = aRepeat;
            Double = false;
        }

        beforeNum = array[a];
        a = a +1;
    }

    if(Double) return -1;
    return i;

    }