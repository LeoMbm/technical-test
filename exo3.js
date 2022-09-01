function getCharCode(sentence) {

    let result = [];
    for (let i = 0; i < sentence.length; i++) {
        result.push(sentence.charCodeAt(i));
    }
    return result;
}

let sentence = "Hello, Nalios !";
console.log(getCharCode(sentence));
// Here i take all the char code and i put all the char code in the method below
console.log(String.fromCharCode(72, 101, 108, 108, 111, 44, 32, 78, 97, 108, 105, 111, 115, 32, 33))



