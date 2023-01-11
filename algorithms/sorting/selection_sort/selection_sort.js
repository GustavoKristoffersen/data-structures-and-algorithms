function selectionSort(arr) {
    for (i=0; i<arr.length; i++) {
        lowestAtIndex = i;
        for (let j=i; j<arr.length; j++) {
            if (arr[j] < arr[lowestAtIndex]) {
                lowestAtIndex = j;
            }
        }
        if (i != lowestAtIndex) {
            let temp = arr[i];
            arr[i] = arr[lowestAtIndex];
            arr[lowestAtIndex] = temp;
        }
    }

    return arr;
}