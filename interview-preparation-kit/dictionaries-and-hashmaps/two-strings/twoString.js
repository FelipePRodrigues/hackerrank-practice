var test = require('./test');
var tests = new test();

twoStrings(tests.test1[0], tests.test1[1]); // YES
twoStrings(tests.test2[0], tests.test1[1]); // NO
twoStrings(tests.test3[0], tests.test1[1]); // YES

function twoStrings(s1, s2){
    let haveSubstring = false;

    for(let i = 0; i < s1.length; i++){
        for(let j = 0; j < s2.length; j++){
            if(s1[i] === s2[j]){
                haveSubstring = true;
                break;              
            }                
        }
    }

    if(haveSubstring == true)
        console.log("Yes");
    else
        console.log("No");
}