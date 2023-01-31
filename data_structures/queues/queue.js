class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}


class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    _isEmpty() {
        return this.first == null && this.last == null;
    }

    // O(1)
    enqueue(value) {
        let newNode = new Node(value);
        if(this._isEmpty()) {
            this.first = this.last = newNode;
        }
        else {
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }
    
    // O(1)
    dequeue() {
        if(this._isEmpty()) {
            return null;
        }
        else if (this.length === 1) {
            this.last = null;
        }
        let nodeToPop = this.first;
        this.first = nodeToPop.next;
        this.length--;
        return nodeToPop;
    }

    // O(1)
    peek() {
        return this._isEmpty()? null: this.first.value;
    }

    printAsList() {
        let array = [];
        let currentNode = this.first;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        console.log(array);
    }
}