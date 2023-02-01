class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}


class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    _isEmpty() {
        return this.head === null && this.tail === null;
    }

    prepend(value) {
        let node = new Node(value);
        if (this._isEmpty()) {
            this.tail = node;
        }
        node.next = this.head;
        this.head = node;
        this.length++;
        return this;
    }

    append(value) {
        let node = new Node(value);
        if (this._isEmpty()) {
            this.head = node;
            this.tail = node;
        }
        else {
            this.tail.next = node;
            this.tail = node;
        }
        this.length++;
        return this;
    }

    insert(index, value) {
        if (index < 0) {
            return this;
        }
        else if (index === 0) {
            return this.prepend(value);
        }
        else if (index >= this.length) {
            return this.append(value);
        }
        let newNode = new Node(value);
        if (this._isEmpty()) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            let leftNode = this._getNodeAtIndex(index - 1);
            let rightNode = leftNode.next;
            leftNode.next = newNode;
            newNode.next = rightNode;
        }
        this.length++;
        return this;
    }

    delete(index) {
        if (index < 0 || index >= this.length) {
            return this
        };
        if (this._isEmpty()) {
            return this;
        }
        else if (index === 0) {
            this.head = this.head.next;
        }
        else {
            let leftNode = this._getNodeAtIndex(index - 1);
            let nodeToBeDeleted = leftNode.next;
            leftNode.next = nodeToBeDeleted.next;
            if (nodeToBeDeleted === this.tail) {
                this.tail = leftNode;
            }
        }
        this.length--;
        return this;
    }

    _getNodeAtIndex(index) {
        let currentNode = this.head;
        let position = 0;
        while (position < index) {
            currentNode = currentNode.next;
            position++;
        }
        return currentNode;
    }

    printAsList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value)
            currentNode = currentNode.next
        }
        console.log(array);
    }

    reverse() {
        if (this.length === 1 || this._isEmpty()) {
            return this;
        }
        let currentNode = this.head;
        let previousNode = null;
        while (currentNode !== null) {
            let nextNode = currentNode.next;
            currentNode.next = previousNode;
            previousNode = currentNode;
            currentNode = nextNode;
        }
        this.tail = this.head;
        this.head = previousNode;
        return this;
    }
}