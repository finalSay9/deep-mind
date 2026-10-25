const numbers: number[] = [1, 2, 3, 4, 5, 6];

for(let n of numbers) {
    const current = numbers[n];
    const next = numbers[n + 1];
    if(current !== undefined && next !== undefined && current > next) {
        numbers[n] = next;
        numbers[n + 1] = current;
    }
}