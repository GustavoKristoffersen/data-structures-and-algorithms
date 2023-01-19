class Stack {
    constructor() {
        this.data = [];
    }

    pop() {
        return this.isEmpty()? null: this.data.pop();
    }

    push(value) {
        this.data.push(value);
        return this;
    }

    peek() {
        return this.isEmpty()? null: this.data[this.data.length - 1];
    }

    isEmpty() {
        return this.data.length === 0;
    }

    printAsList() {
        console.log(this.data);
    }
}