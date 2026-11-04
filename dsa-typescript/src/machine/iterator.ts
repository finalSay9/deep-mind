const numberCollection = {
    [Symbol.iterator]() {
        let current = 1;
        const maximum = 5;

        return {
            next() {
                if (current <= maximum) {
                    return {
                        value: current++,
                        done: false
                    };
                }

                return {
                    value: undefined,
                    done: true
                };
            }
        };
    }
};

for (const number of numberCollection) {
    console.log(number);
}
