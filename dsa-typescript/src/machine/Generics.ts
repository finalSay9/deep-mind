function processIdentifier(identifier: string | number): void {
    if(typeof identifier == 'string') {
        console.log(identifier.toLocaleUpperCase())
    } else {
        console.log(identifier.toFixed(2));
    }
    
}