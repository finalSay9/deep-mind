
interface Product {
    name: string;
    price: number;
    quantity: number;
}

const products: Product[] = [
    {name: 'iphone', price: 905000, quantity: 45},
    {name: 'vivo', price: 1320, quantity: 44},
    {name: 'samsung', price: 8891500, quantity: 34},
    {name: 'pixel', price: 60000, quantity: 23}
]

let total = 0
let expensive: Product | undefined = products[0]
let cheap: Product | undefined = products[0]


for(let product of products) {
    let sum = 0;
    sum += product.price * product.quantity
    console.log(`${product.name} : ${sum}`)
    total += product.price * product.quantity
}

//find an item that is expensive
for(let product of products) {
    if(expensive === undefined || product.price > expensive.price) {
        expensive = product
    }
    
}


for(let product of products) {
    if(cheap === undefined || product.price < cheap.price) {
        cheap = product
    }
    
}

console.log(`Total Value: ${total}`);
// 3. Now you can cleanly print both the name and price at the very end
if (expensive !== undefined) {
    console.log(`Most Expensive Item: ${expensive.name} (${expensive.price})`)
}

if (cheap !== undefined) {
    console.log(`Most Cheap Item: ${cheap.name} (${cheap.price})`)
}