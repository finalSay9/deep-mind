
function facto(num: number) {
    if(num ===0 || num === 1) {
        return 1
    }
    else {
        num * facto(num - 1)
    }
}