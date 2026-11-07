function countDown(counting: number): number {
    console.log(counting);

    if(counting < 0) {
        console.log("cant bt defined in negative numbers");
    }
    if(counting === 0 || counting === 1) {
        return 1;
    }

   return counting * countDown(counting - 1)

}

console.log(countDown(5))