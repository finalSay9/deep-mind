
function facto(num: number): number {
    if(num ===0 || num === 1) {
        return 1
    }
    else {
       return num * facto(num - 1)
    }
}
//now lets call the fanction facto to compute our factorial
let result: number = facto(5)
console.log(result)