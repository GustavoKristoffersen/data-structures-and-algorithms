function breadthFirstSearch(root) {
    let result = [];
    let queue = [];

    queue.push(root);

    while (queue.length > 0) {
        let currentNode = queue.shift();
        result.push(currentNode.value);
        if (currentNode.left) {
            queue.push(currentNode.left);
        }
        if (currentNode.right) {
            queue.push(currentNode.right);
        }
    }

    return result;
}

function breadthFirstSearchRecursive(queue, result=[]) {
    if (!queue.length > 0) {
        return result;
    }

    let currentNode = queue.shift();
    result.push(currentNode.value);
    if (currentNode.left) {
        queue.push(currentNode.left);
    }
    if (currentNode.right) { 
        queue.push(currentNode.right);
    }

    return breadthFirstSearchRecursive(queue, result);
}