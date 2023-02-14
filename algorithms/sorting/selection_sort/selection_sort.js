function selectionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let lowestAtIndex = i;

        for (let j = i+1; j < arr.length; j++) {
            if (arr[j] < arr[lowestAtIndex]) {
                lowestAtIndex = j;
            }
        }

        if (lowestAtIndex !== i) {
            let temp = arr[i];
            arr[i] = arr[lowestAtIndex];
            arr[lowestAtIndex] = temp;
        }
    }
    return arr;
}