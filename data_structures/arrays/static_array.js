const {linearSearch} = require('../../algorithms/searching/linear_search/linear_search.js')


class StaticArray {
    constructor(length) {
        this.length = length;
        this.values = new Array(length).fill(null);
    }

    // O(1)
    insert(index, value) {
        if (index >= this.length) {
          return null;
        }
        this.values[index] = value;
        return this;
    }
      
    // O(1)
    delete(index) {
        if (index >= this.length) {
            return null;
        }
        this.values[index] = null;
        return this;
    }

    linearSearch(value) {
        return linearSearch(this.values, value);
    }
}

