interface Admin {
    name: string;
    permissions: string[];
}

interface Customer {
    name: string;
    purchaseHistory: string[];
}

const admin: Admin[] = [
    {name: 'lesono', permissions: ['can sell', 'delete', 'create account']},
    {name: 'uchie', permissions: ['can sell',  'create account']},
    {name: 'levante', permissions: ['delete', 'create account']}
]

const customer: Customer[] = [
    {name: 'evan', purchaseHistory: ['iphone', 'vivo', 'pixel']},
    {name: 'mercy', purchaseHistory: ['iphone', 'vivo', 'pixel', 'samsung']},
    {name: 'loyis', purchaseHistory: ['xiaomi', 'vivo', 'pixel']},
]



function displayUser(user: Admin | Customer): void {
    
    console.log(user.name);
    if("permissions" in user) {
        console.log(user.permissions)
    }
    else {
        console.log(user.purchaseHistory)
    }
}
// Find the customer object named 'evan'
const evanCustomer = customer.find(c => c.name === 'lesono');

// Make sure evan was found, then display him
if (evanCustomer) {
    displayUser(evanCustomer);
} else {
    console.log("Customer not found");
}
