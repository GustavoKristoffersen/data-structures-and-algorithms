// using nested for loops
function bubbleSort(arr) {
    for (i=0; i<arr.length; i++) {
        for (let j=0; j<arr.length-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                let temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
    }

    return arr;
}

// using a while loop (more descriptive)
function bubbleSort(arr) {
    let unsortedUntilIndex = arr.length - 1;
    let sorted = false;

    while (!sorted) {
        sorted = true;
        for (let i = 0; i < unsortedUntilIndex; i++) {
            if (arr[i] > arr[i + 1]) {
                let temp = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = temp;
                sorted = false;
            }
        }
        unsortedUntilIndex--;
    }
    return arr;
}