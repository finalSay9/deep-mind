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

class PaymentService {
    constructor(
        private readonly paymentMethod: PaymentMethod
    ) {}

    pay(amount: number): void {
        this.paymentMethod.process(amount)
    }
}

const payment = new PaymentService(
    new MobilePayment()
)
payment.pay(100000)