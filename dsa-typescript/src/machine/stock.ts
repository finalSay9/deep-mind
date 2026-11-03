
interface Product {
    name: string;
    price: number;
    quantity: number;
}

const products: Product[] = [
    {name: 'iphone', price: 1200, quantity: 45},
    {name: 'vivo', price: 1320, quantity: 44},
    {name: 'samsung', price: 1500, quantity: 34},
    {name: 'pixel', price: 1600, quantity: 23}
]

let total = 0


for(let product of products) {
    total += product.price * product.quantity
}

console.log(total)