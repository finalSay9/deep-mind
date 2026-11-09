class Payment {
    process(amount: number): void {
        console.log(`processing ${amount}`)
    }
}

class CardPayement extends Payment{
    process(amount: number): void {
        console.log(`processing card payment ${amount}`)
    }
}

class MobilePayment extends Payment {
    process(amount: number): void {
        console.log(`processing mobile payment ${amount}`)
    }
}

const payments: Payment[] = [
    new CardPayement(),
    new MobilePayment()
]

for(const pay of payments){
    pay.process(10000)
}

