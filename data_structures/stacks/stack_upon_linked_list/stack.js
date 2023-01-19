class Node {
    constructor (value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    pop() {
        if (this.isEmpty()) {
            return null;
        }
        if (this.length === 1) {
            this.bottom = null;
        }
        let nodeToPop = this.top;
        let nodeBelow = this.top.next;
        this.top = nodeBelow;
        this.length--;
        return nodeToPop.value;
    }

    push(value) {
        let newNode = new Node(value);
        if (this.isEmpty()) {
            this.bottom = this.top = newNode;
        }
        else {
            newNode.next = this.top;
            this.top = newNode;
        }
        this.length++;
        return this;
    }

    peek() {
        return this.top === null? null: this.top.value;
    }

    isEmpty() {
        return this.top === null && this.bottom === null;
    }

    printAsList() {
        let array = [];
        let currentNode = this.top;
        while (currentNode != null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        console.log(array);
    }
}