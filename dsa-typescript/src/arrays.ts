
const add = (a: number, b: number): number => {
    return a + b;
}
console.log(add(18,18))
type User = {
    name: string;
    age: number;
    email: string;
    address: string;
}

const user: User = {
    name: 'evan',
    age: 23,
    email: 'evan@gmail.com',
    address: 'lilongwe'
}

console.log(user)

//inheritance interfaces

interface client  {name: string};
interface VipClient extends client {discount: number}

const details: VipClient = {
    name: 'evan',
    discount: 12.3
}

console.log(details)

type member = {
    name: string
}
type VipMember = member & {address: string}

const data: VipMember = {
    name: 'evan chimwaza',
    address: 'aliko street'
}

console.log(data)