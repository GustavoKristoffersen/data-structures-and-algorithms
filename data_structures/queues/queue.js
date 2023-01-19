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

    enqueue(value) {
        let newNode = new Node(value);
        if(this.isEmpty()) {
            this.first = this.last = newNode;
        }
        else {
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }

    dequeue() {
        if(this.isEmpty()) {
            return null;
        }
        else if (this.length === 1) {
            this.first = null;
        }
        let nodeToPop = this.first;
        this.first = nodeToPop.next;
        this.length--;
        return nodeToPop;
    }

    peek() {
        return this.isEmpty()? null: this.first.value;
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

    isEmpty() {
        return this.first == null && this.last == null;
    }
}