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
      let item = this.data[this.length-1];
      delete this.data[this.length-1];
      this.length--;
      return item;
    }
    
    // O(1)
    get(index) {
      return this.data[index];
    }
  
    performShiftingsToRight(index) {
      for(let i=this.length - 1; i > index; i--) {
        this.data[i] = this.data[i-1];
      }
    }
    
    // O(n)
    insert(value, index) {
      this.length++;
      this.performShiftingsToRight(index);
      this.data[index] = value;
      return this.data;
    }
  
    performShiftingsToLeft(index) {
      for(let i=index; i < this.length - 1; i++) {
        this.data[i] = this.data[i+1];
      }
      delete this.data[this.length - 1];
    }
    
    // O(n)
    delete(index) {
      let item = this.data[index];
      delete this.data[index];
      this.performShiftingsToLeft(index);
      this.length--;
      return this.length;
    }
  }