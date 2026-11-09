class LoanCalculate {
        calculateInterest(amount: number, rate: number): number {
            return amount * rate/100
        }
}

class LoanRepository {
    save(loan: object): void {
        console.log(`saving loan ${loan}`)
    }
}

class EmailService {
    sendEmail(message: string): void {
        console.log(`sending email ${message}`);
    }
}

const loan = new LoanCalculate()
console.log(loan.calculateInterest(3420, 12.12))