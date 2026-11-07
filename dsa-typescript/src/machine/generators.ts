async function* generateData(){
    yield 100;
    yield 200;
    yield 300;

    return "operation complete"
}

async function main() {
    const generator = generateData();

    console.log(await generator.next());
    console.log(await generator.next());
    console.log(await generator.next());
    console.log(await generator.next());
}

main();