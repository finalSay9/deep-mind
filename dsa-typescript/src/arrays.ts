type Address = {
    name: string,
    id: number
}

interface Company {
    name: string,
    address: Address,
    no_of_employees: number,
    departments: number,
    registered: boolean
}

interface Person extends Company {
    email: string,
    age: number,
}

const info: Person = {
    name: 'techvach',
    address: {
        name: 'welo street',
        id: 1234
    },
    no_of_employees: 343,
    departments: 34,
    registered: true,
    email: 'evanchimwaza@gmail.com',
    age: 23
}
console.log(info)