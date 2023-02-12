class Array {
    constructor() {
      this.length = 0;
      this.data = {};
    }
    
    // O(1)
    push(value) {
      this.data[this.length] = value;
      this.length++
      return this.data;
    }
    
    // O(1)
    pop() {
      if (!this.length > 0) {
        return null;
      }
      let item = this.data[this.length-1];
      delete this.data[this.length-1];
      this.length--;
      return item;
    }
    
    // O(1)
    get(index) {
      return index < this.length? this.data[index]: null;
    }
  
    _performShiftingsToRight(index) {
      for(let i=this.length; i > index; i--) {
        this.data[i] = this.data[i-1];
      }
    }
    
    // O(n)
    insert(value, index) {
      if (index > this.length) {
        return null;
      }
      this._performShiftingsToRight(index);
      this.data[index] = value;
      this.length++;
      return this.data;
    }
  
    _performShiftingsToLeft(index) {
      for(let i=index; i < this.length - 1; i++) {
        this.data[i] = this.data[i+1];
      }
    }
    
    // O(n)
    delete(index) {
      if (index > this.length - 1) {
        return null;
      }
      this._performShiftingsToLeft(index);
      delete this.data[this.length-1];
      this.length--;
      return this.length;
    }
  }