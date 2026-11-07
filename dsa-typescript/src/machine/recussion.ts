function countDown(counting: number): void {
    console.log(counting);

    if(counting == 0) {
        return;
    }

    else{
        countDown((counting - 1) * counting)
    }

}

countDown(5)