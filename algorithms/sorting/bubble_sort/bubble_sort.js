// using nested for loops
function bubbleSort(arr) {
    for (i=0; i<arr.length; i++) {
        for (j=0; j<arr.length-i-1; j++) {
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
    var unsortedUntilIndex = arr.length - 1;
    var sorted = false;

    while (!sorted) {
        sorted = true;
        for (var i = 0; i < unsortedUntilIndex; i++) {
            if (arr[i] > arr[i + 1]) {
                var temp = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = temp;
                sorted = false;
            }
        }
        unsortedUntilIndex--;
    }
    return arr;
}