const numbers = [1,2,3,4,0,6]


for(let i = 0; i < numbers.length -1; i++) {

for(let a of numbers){
    if(numbers[a] > numbers[a+1]) {
        [numbers[a], numbers[a+1]] = [numbers[a+1], numbers[a]]
        
    }
}
}
console.log(numbers)