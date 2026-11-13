interface Transaction {
    id: number;
    user: string;
    amount: number;
    type: "DEPOSIT" | "WITHDRAWAL";
    status: "SUCCESS" | "FAILED" | "PENDING";
}

const transactions: Transaction[] = [
    { id: 1, user: "Evan", amount: 5000, type: "DEPOSIT", status: "SUCCESS" },
    { id: 2, user: "John", amount: 2000, type: "WITHDRAWAL", status: "SUCCESS" },
    { id: 3, user: "Mary", amount: 3000, type: "DEPOSIT", status: "FAILED" },
    { id: 4, user: "Evan", amount: 1500, type: "WITHDRAWAL", status: "SUCCESS" },
    { id: 5, user: "Peter", amount: 7000, type: "DEPOSIT", status: "PENDING" },
    { id: 6, user: "Mary", amount: 4000, type: "DEPOSIT", status: "SUCCESS" }
];

//retrive all successful transactions
const successful = transactions.filter((client) => {
    return client.status === "SUCCESS";
})
console.log(successful)

//getting all deposite transactions
const all_deposit = transactions.filter((deposit) => {
    return deposit.type === "DEPOSIT";
})
console.log(all_deposit)

//extracting only the transaction amounts
const all_amounts = transactions.map((transactionAmaount) => {
    return transactionAmaount.amount;
})
console.log(all_amounts)

//calculate all successful deposites

const deposites = transactions
                .filter((success) => success.type === "DEPOSIT" && success.status ==="SUCCESS")
                .reduce((total, current) => total + current.amount,
            0)
console.log(deposites)


//find Evan's successful transactions
const evan = transactions.find((succes) => 
    succes.user === "Evan" && succes.status === "SUCCESS"
)
console.log(evan)

//check for large transaction
const larger = transactions.some((large) => {
    large.status === "SUCCESS" && large.amount > 5000
})
console.log(larger)

const check = transactions.every((large) => large.amount > 5000)
console.log(check)

//all to mary
const mary = transactions
            .filter((name) => name.user ==="Mary")
            .map((trans) => trans.amount)

console.log(mary)