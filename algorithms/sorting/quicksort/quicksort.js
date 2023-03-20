class QuickSort {
    constructor(array) {
        this.array = array;
    }


    partition(leftIndex, rightIndex) {
        let pivotIndex = rightIndex;
        let pivot = this.array[pivotIndex];
        rightIndex--;
        
        while(true) {

            while (this.array[leftIndex] < pivot) {
                leftIndex++;
            }

            while (this.array[rightIndex] > pivot) {
                rightIndex--;
            }

            if (leftIndex >= rightIndex) {
                break;
            }
            else {
                let tempLeft = this.array[leftIndex];
                this.array[leftIndex] = this.array[rightIndex];
                this.array[rightIndex] = tempLeft;
                leftIndex++;
            }
        }

        let tempLeft = this.array[leftIndex];
        this.array[leftIndex] = pivot;
        this.array[pivotIndex] = tempLeft;
        
        return leftIndex;
    }
    
    quicksort(leftIndex, rightIndex) {
        if (rightIndex - leftIndex <= 0) {
            return;
        }

        let pivotIndex = this.partition(leftIndex, rightIndex);
        this.quicksort(leftIndex, pivotIndex - 1);
        this.quicksort(pivotIndex + 1, rightIndex);
    }

    sort() {
        this.quicksort(0, this.array.length - 1);
        return this.array;
    }
}