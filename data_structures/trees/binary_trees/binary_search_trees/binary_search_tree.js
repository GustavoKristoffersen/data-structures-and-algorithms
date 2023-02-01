class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}


class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  // O(log N)
  insert(value) {
    let newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
      return this;
    }
    let currentNode = this.root;
    while (true) {
      if (value < currentNode.value) {
        if (currentNode.left === null) {
          currentNode.left = newNode;
          return this;
        }
        currentNode = currentNode.left;
      }
      else if (value > currentNode.value) {
        if (currentNode.right === null) {
          currentNode.right = newNode;
          return this;
        }
        currentNode = currentNode.right;
      }
      else {
        return this;
      }
    }
  }

  // O(log N)
  search(value) {
    let currentNode = this.root;
    while (currentNode !== null) {
      if (value === currentNode.value) {
        return currentNode;
      }
      if (value < currentNode.value) {
        currentNode = currentNode.left;
      }
      else {
        currentNode = currentNode.right;
      }
    }
    return null;
  }

  // O(log N)
  remove(value) {
    let currentNode = this.root;
    let parentNode = null;

    while (currentNode !== null) {
      if (value < currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.left;
      }
      else if (value > currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.right;
      }
      else if (currentNode.value === value) {

        // Option 1: No right child
        if (currentNode.right === null) {
          if (parentNode === null) {
            this.root = currentNode.left;
          }
          else {
            // if current value < parent, make current node left child a child of parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.left;

            }
            // if current value > parent, make left child a right child of parent
            else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.left;
            }
          }
        }

        //Option 2: Right child which doesnt have a left child
        else if (currentNode.right.left === null) {
          currentNode.right.left = currentNode.left;
          if (parentNode === null) {
            this.root = currentNode.right;
          }
          else {
            // if parent > current, make right child of the left the parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.right;

            }
            // if parent < current, make right child a right child of the parent
            else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.right;
            }
          }
        }

        //Option 3: Right child that has a left child
        else {

          //find the Right child's left most child
          let leftmost = currentNode.right.left;
          let leftmostParent = currentNode.right;
          while (leftmost.left !== null) {
            leftmostParent = leftmost;
            leftmost = leftmost.left;
          }

          //Parent's left subtree is now leftmost's right subtree
          leftmostParent.left = leftmost.right;
          leftmost.left = currentNode.left;
          leftmost.right = currentNode.right;

          if (parentNode === null) {
            this.root = leftmost;
          }
          else {
            if (currentNode.value < parentNode.value) {
              parentNode.left = leftmost;
            }
            else if (currentNode.value > parentNode.value) {
              parentNode.right = leftmost;
            }
          }
        }
        return true;
      }
    }
    return false;
  }

}