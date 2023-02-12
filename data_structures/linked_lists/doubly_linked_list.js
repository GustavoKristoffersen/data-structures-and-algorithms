class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.previous = null;
    }
}


class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    // O(N)
    insert(index, value) {
        if (index < 0) {return this};

        let newNode = new Node(value);
        if (this._isEmpty()) {
            this.head = this.tail = newNode;
        }
        else if (index === 0) {
            return this.prepend(value);
        }
        else if (index >= this.length) {
            return this.append(value);
        }
        else {
            let leftNode = this._getNodeAtIndex(index - 1);
            let rightNode = leftNode.next;
            leftNode.next = newNode;
            newNode.next = rightNode;
            newNode.previous = leftNode;
            rightNode.previous = newNode;
        }
        this.length++;
        return this;
    }

    // O(N)
    delete(index) {
        if (index < 0 || index >= this.length) {return this};
        
        if (this._isEmpty()) {
            return this;
        }
        else if (index === 0){
            this.head = this.head.next;
            this.head.previous = null;
            this.head.next.previous = this.head;
        }
        else {
            let leftNode = this._getNodeAtIndex(index - 1);
            let nodeToBeDeleted = leftNode.next;
            let rightNode = nodeToBeDeleted.next;
            leftNode.next = rightNode;
            rightNode.previous = leftNode;
            if (nodeToBeDeleted === this.tail) {
                this.tail = leftNode;
            }
        }
        this.length--;
        return this;
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
        }
        else {
            this.tail.next = node;
        }
        node.previous = this.tail;
        this.tail = node;
        this.length++;
        return this;
    }

    printList() {
        const array = [];
        let currentNode = this.head;
        while(currentNode !== null){
            array.push(currentNode.value)
            currentNode = currentNode.next
        }
        console.log(array);
    }

    _isEmpty() {
        return this.head === null && this.tail === null;
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
}