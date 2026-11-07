interface Employee {
    id: number;
    name: string;
    department: string;
    salary: number;
}

const employees: Employee[] = [
    { id: 1, name: "Evan", department: "Engineering", salary: 5000 },
    { id: 2, name: "John", department: "Marketing", salary: 2500 },
    { id: 3, name: "Mary", department: "Engineering", salary: 4500 },
    { id: 4, name: "Peter", department: "Finance", salary: 3500 },
    { id: 5, name: "Grace", department: "Marketing", salary: 4000 }
];

//earning above 3000
const user = employees.filter((employee) => {
    const earning = employee.salary > 3000;
    return earning;
})
console.log(user)

//get all employees names
const names = employees.map((employee) => {
    const all_names = employee.name
    return all_names;
})
console.log(names)

//calculate total saraly
let total = 0;
const salary_expenditure = employees.reduce((sum, current) => {
    return sum + current.salary;
}, 0);
console.log(`Total Salary Expenditure: ${salary_expenditure}`);

//find mary by name
const user_by_name = employees.find((employee) => {
    if(employee.name === "Mary") {
        return employee.name
    }

})
console.log(user_by_name)

//check whether everyone earns above 6000
const check = employees.some((employee) => employee.salary >= 6000)
console.log(check)

//chech whether everyone earn at least 2000
const checkif = employees.every((employee) => employee.salary <= 2000)
console.log(checkif)

const engeens = employees
                .filter((employee) => employee.department ==="Engineering")
                .map((employee: Employee) => employee.name)

console.log(engeens)