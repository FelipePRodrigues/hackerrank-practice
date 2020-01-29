var teste1 = {magazine:["give", "me", "one", "grand", "today", "night"], note:["give", "one", "grand", "today"]} // YES
var teste2 = {magazine:["two","times","three","is","not","four"], note:["two","times","two","is","four"]} // NO
var teste3 = {magazine:["ive", "got", "a", "lovely", "bunch", "of", "coconuts"], note:["ive", "got", "some", "coconuts"]} // NO

var magazine = [];

checkMagazine(teste1.magazine, teste1.note);
checkMagazine(teste2.magazine, teste2.note);
checkMagazine(teste3.magazine, teste3.note);

function checkMagazine(magazineTest, notes) {    
    magazine = magazineTest;

    let allNotesAreInMagazine = true;

    for(let i = 0; i < notes.length; i++){
        if(!isNoteInMagazine(notes[i])){
            allNotesAreInMagazine = false;
            break;
        }        
    }   

    if(allNotesAreInMagazine){
        console.log("Yes");
    }
    else{
        console.log("No");
    }
    
}

function isNoteInMagazine(note){
    for(let i = 0; i < magazine.length; i++){
        if(note == magazine[i]){
            removeNoteFromMagazine(note);
            return true;
        }
    }
}

function removeNoteFromMagazine(note){
    const index = magazine.indexOf(note);
    
    if (index > -1) {
        magazine.splice(index, 1);
    }
}