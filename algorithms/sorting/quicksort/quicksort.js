function partition(array, leftIndex, rightIndex) {
    let pivotIndex = rightIndex;
    let pivot = array[pivotIndex];
    rightIndex = rightIndex - 1;

    while (true) {
        while (array[leftIndex] < pivot) {
            leftIndex++;
        }

        while (array[rightIndex] > pivot) {
            rightIndex--;
        }

        if (leftIndex >= rightIndex) {
            break;
        }
        else {
            let tempLeft = array[leftIndex];
            array[leftIndex] = array[rightIndex];
            array[rightIndex] = tempLeft;
            leftIndex++;
        }
    }

    let tempLeft = array[leftIndex];
    array[leftIndex] = pivot;
    array[pivotIndex] = tempLeft;

    return leftIndex;
}

function quicksort(array, leftIndex, rightIndex) {
    if (!leftIndex && !rightIndex) {
        leftIndex = 0;
        rightIndex = array.length - 1;
    }
    
    if (rightIndex - leftIndex <= 0) {
        return;
    }

    let pivotIndex = partition(array, leftIndex, rightIndex);
    quicksort(array, leftIndex, pivotIndex - 1);
    quicksort(array, pivotIndex + 1, rightIndex);

    return array;
}