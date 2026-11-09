interface PaymentMethod {
    process(amount: number): void;
}

class CardPayment implements PaymentMethod {
    process(amount: number): void {
        console.log(`processing card payment ${amount}`)
    }
}

class MobilePayment implements PaymentMethod {
    process(amount: number): void {
        console.log(`processing mobile payment ${amount}`)
    }
}