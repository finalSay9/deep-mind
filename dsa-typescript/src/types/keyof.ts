class Loan {
    borrower: string;
    amount: number;
    intrestRate: number;

    constructor(
        borrower: string,
        amount: number,
        intrestRate: number,
    ) {
        this.borrower = borrower,
        this.amount = amount,
        this.intrestRate = intrestRate
    }

    calculateInterest(): number {
        return this.amount * this.intrestRate/100
    }
}
const loan1 = new Loan("Evan", 100000, 15);
const loan2 = new Loan("John", 50000, 12);

console.log(loan1.calculateInterest()); // 15000
console.log(loan2.calculateInterest()); // 6000