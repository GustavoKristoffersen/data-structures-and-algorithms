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