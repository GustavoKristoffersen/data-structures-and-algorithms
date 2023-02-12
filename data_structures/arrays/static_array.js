const {linearSearch} = require('../../algorithms/searching/linear_search/linear_search.js')


class StaticArray {
    constructor(length) {
        this.length = length;
        this.last_position = -1;
        this.values = new Array(length).fill(null);
    }

    add(value) {
        // no space left
        if (this.last_position === this.length - 1) {
            return null;
        }
        this.last_position += 1;
        this.values[this.last_position] = value;
        return this;
    }

    delete(value) {
        let p = linearSearch(value);
        if (p === -1) {
            return -1;
        }
        for (let i = p; i < this.last_position; i++) {
            this.values[i] = this.values[i + 1];
        }
        this.last_position--;
        return this;
    }

    linearSearch(value) {
        return linearSearch(this.values, value);
    }
}

