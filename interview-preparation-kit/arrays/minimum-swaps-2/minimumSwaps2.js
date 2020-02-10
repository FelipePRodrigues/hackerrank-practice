var test1 = [1,3,2,4]; //1
var test2 = [1,5,6,7,3,2,4]; // 4
var test3 = [2,31,1,38,29,5,44,6,12,18,39,9,48,49,13,11,7,27,14,33,50,21,46,23,15,26,8,47,40,3,32,22,34,42,16,41,24,10,4,28,36,30,37,35,20,17,45,43,25,19]; // 46

minimumSwaps(test1);
minimumSwaps(test2);
minimumSwaps(test3);

var temporaryArray = [];

function minimumSwaps(test) {
    temporaryArray = [];
    let aux = 0;
    
    for(let i = 0; i < test.length; i++){
        if(test[i] != (i+1)){
            aux = aux + 1;            
            test = swapArray(i, test);            
        }
    }
    
    console.log(aux);    
}

function swapArray(currentIndex, test){
    for(let i = currentIndex; i < test.length; i++){
        
        if(test[i] == (currentIndex + 1)){
            let aux = test[currentIndex];
            test[currentIndex] = aux;
            test[i] = aux;
            return test;
        }
        
    }
    
    return test;
}