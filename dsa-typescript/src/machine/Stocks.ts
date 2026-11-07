interface User {
    id: number;
    name: string;
    email: string;
}


const users: User[] = [
    {id: 1, name: "Evan", email: "evan@gmail.com"},
    {id: 2, name: "teeya", email: "tiya@gmail.com"},
    {id: 3, name: "joy", email: "joy@gmail.com"}
];


function findUser(id: number): User | undefined;
function findUser(email: string): User | undefined;


function findUser(identifier: number | string): User | undefined {
    if(typeof identifier =='number') {
        return users.find((user) => user.id === identifier)
    }

    return users.find((user) => user.email == identifier)
}

console.log(findUser(1))
console.log(findUser('joy@gmail.com'))