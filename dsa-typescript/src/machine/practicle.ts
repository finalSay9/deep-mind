function createBankAccount(balance: number) {
        balance = 1000;

        return {
        deposit(amount: number) {
            balance += amount;
            return balance;
        },

        withdraw(amount: number) {
            balance -= amount;
            return balance
        },

        getBalance() {
            return balance;
        }
    }
        
}

const result = createBankAccount(1000)
console.log(result.deposit(9000))
console.log(result.withdraw(3400))
console.log(result.getBalance())