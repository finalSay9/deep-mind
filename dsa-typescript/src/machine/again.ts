interface Employee {
    id: number;
    name: string;
    salary: number;
}

const employees: Employee[] = [
    { id: 1, name: "Evan", salary: 5000 },
    { id: 2, name: "John", salary: 3000 },
    { id: 3, name: "Mary", salary: 4500 },
    { id: 4, name: "Peter", salary: 2500 }
];

let higher: Employee | undefined = employees[0]

const money = employees.map((employee) => {
    if(higher === undefined || employee.salary  > higher.salary) {
        higher = money

    }
})


console.log(higher)