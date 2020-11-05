numbers = [1, 2]
i = 2
z =20
process.stdout.write(numbers[0].toString() + " \n");
process.stdout.write(numbers[1].toString() + " ");
process.stdout.write(numbers[1].toString() + " \n");

while(i<z) {
    numbers[i] = numbers[i-1] + numbers[i-2];
    for(j = 0; j < i+1; j++) {
        process.stdout.write(numbers[i].toString() + " ");
    }

    console.log(" ")
    i = i+1;
}