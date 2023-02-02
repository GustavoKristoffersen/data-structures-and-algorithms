class Heap {
    constructor() {
        this.data = [];
        this.length = 0;
    }

    root() {
        return this.data[0];
    }

    last() {
        return this.data[this.data.length - 1];
    }

    printAsList() {
        console.log(this.data);
    }

    _getLeftChildIndex(index) {
        return (index * 2) + 1;
    }

    _getRightChildIndex(index) {
        return (index * 2) + 2;
    }

    _getParentIndex(index) {
        return parseInt((index - 1) / 2);
    }

    // O(log N)
    insert(value) {
        this.data.push(value);
        let newNodeIndex = this.data.length - 1;
        let parentIndex = this._getParentIndex(newNodeIndex);
        while (newNodeIndex > 0 && this.data[newNodeIndex] > this.data[parentIndex]) {
            let tempParentValue = this.data[parentIndex];
            this.data[parentIndex] = this.data[newNodeIndex];
            this.data[newNodeIndex] = tempParentValue;

            newNodeIndex = parentIndex;
            parentIndex = this._getParentIndex(newNodeIndex);
        }
        this.length++;
        return this;
    }

    // O(log N)
    delete() {
        if (!this.data) {
            return;
        }
        this.data[0] = this.data.pop();
        let trickleNodeIndex = 0;

        while (this._hasChildrenWithGreaterValue(trickleNodeIndex)) {
            let greatestChildIndex = this._getGreatestChildIndex(trickleNodeIndex);
            let tempGreatestChild = this.data[greatestChildIndex];
            this.data[greatestChildIndex] = this.data[trickleNodeIndex];
            this.data[trickleNodeIndex] = tempGreatestChild;

            trickleNodeIndex = greatestChildIndex;
        }
        this.length--;
        return this;
    }

    _hasChildrenWithGreaterValue(index) {
        let trickleNode = this.data[index];
        let leftChild = this.data[this._getLeftChildIndex(index)];
        let rightChild = this.data[this._getRightChildIndex(index)];
        return (leftChild && leftChild > trickleNode) || (rightChild && rightChild > trickleNode);
    }

    _getGreatestChildIndex(index) {
        let leftChild = this.data[this._getLeftChildIndex(index)];
        let rightChild = this.data[this._getRightChildIndex(index)];
        if (!rightChild) {
            return this._getLeftChildIndex(index);
        }
        if (rightChild > leftChild) {
            return this._getRightChildIndex(index);
        }
        else {
            return this._getLeftChildIndex(index);
        }
    }
}