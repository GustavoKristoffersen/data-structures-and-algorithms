function binarySearch(arr, value) {
    leftIndex = 0;
    rightIndex = arr.length - 1;
    
    while (leftIndex <= rightIndex) {
        middleIndex = Math.floor((leftIndex + rightIndex) / 2);
        middleValue = arr[middleIndex];
        
        if (middleValue === value) {
            return middleIndex;
        }
        else if (middleValue > value) {
            rightIndex = middleIndex - 1;
        }
        else {
            leftIndex = middleIndex + 1;
        }
    }

    return -1;
}