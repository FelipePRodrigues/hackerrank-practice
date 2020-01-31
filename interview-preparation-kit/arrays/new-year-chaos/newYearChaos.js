minimumBribes([2,1,5,3,4]); // 3
minimumBribes([2,5,1,3,4]); // Too chaotic
minimumBribes([5,1,2,3,7,8,6,4]); // Too chaotic
minimumBribes([1,2,5,3,7,8,6,4]); // 7
minimumBribes([1,2,5,3,4,7,8,6]); // 4

function minimumBribes(line) {   
    let bribes = 0;

    line.forEach(function(item, index){
        line[index] = line[index] - 1;
    });

    for(let i = 0; i < line.length; i++){
        if(line[i] - i > 2){
            console.log("Too chaotic");
            return;
        }         
    }

    console.log("Talvez");
}