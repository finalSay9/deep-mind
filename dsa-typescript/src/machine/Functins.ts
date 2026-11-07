function calculate(a: number, b:number): number {
    return a * b;
}

const result = calculate(90,40);
console.log(result)


function processNum(
    number: number,
    operation: (value: number) => number): number {
        return operation(number)
    }


const double = (value: number): number => value * 2;
const square = (value: number): number => value * value;

console.log(processNum(10, double));
console.log(processNum(10, square))


//clousures and lexical

function createCounter() {
    let count = 0;

    function increment() {
        count++;
        console.log(count);
    }
    return increment
}

const counter = createCounter()
counter()