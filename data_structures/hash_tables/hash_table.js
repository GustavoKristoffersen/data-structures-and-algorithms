class HashTable {
    constructor(size) {
        this.data = Array(size).fill(null);
    }

    _hash(key) {
        let hash = 0;
        for (let i =0; i < key.length; i++){
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }

    set(key, value) {
        let address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, value]);
        return this.data;
    }

    get(key) {
        let address = this._hash(key);
        let bucket = this.data[address];
        if (bucket) {
            for (let i=0; i < bucket.length; i++) {
                if (bucket[i][0] === key) {
                    return bucket[i][1];
                }
            }
        }
        return undefined;
    }

    delete(key) {
        let address = this._hash(key);
        let bucket = this.data[address];
        if (bucket) {
            for (let i=0; i < bucket.length; i++) {
                if (bucket[i][0] === key) {
                    let removedValue = bucket[i][1];
                    bucket.splice(i, 1);
                    return removedValue;
                }
            }
        }
        return undefined;
    }

    keys() {
        const keys = [];
        for (let i=0; i < this.data.length; i++) {
            let bucket = this.data[i];
            if(bucket){
                for (let j=0; j < bucket.length; j++) {
                    keys.push(bucket[j][0]);
                }
            }
        }
        return keys;
    }
}
