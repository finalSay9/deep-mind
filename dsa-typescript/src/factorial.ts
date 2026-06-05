
function facto(num: number): number {
    //if num is 0 or 1 give us 1 
    if(num ===0 || num === 1) {
        return 1
    }
    //if its above 1 compute the factorial
    else {
       return num * facto(num - 1)
    }
}
//now lets call the fanction facto to compute our factorial
let result: number = facto(5)
console.log(result)