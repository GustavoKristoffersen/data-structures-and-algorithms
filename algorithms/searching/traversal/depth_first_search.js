function depthFirstSearchPreOrder(currentNode, result=[]) {
    result.push(currentNode.value);

    if (currentNode.left) {
        depthFirstSearchPreOrder(currentNode.left, result);
    }
    if (currentNode.right) {
        depthFirstSearchPreOrder(currentNode.right, result);
    }

    return result;
}


function depthFirstSearchInOrder(currentNode, result=[]) {
    if (currentNode.left) {
        depthFirstSearchInOrder(currentNode.left, result);
    }

    result.push(currentNode.value);

    if (currentNode.right) {
        depthFirstSearchInOrder(currentNode.right, result);
    }

    return result;
}


function depthFirstSearchPostOrder(currentNode, result=[]) {
    if (currentNode.left) {
        depthFirstSearchPostOrder(currentNode.left, result);
    }
    if (currentNode.right) {
        depthFirstSearchPostOrder(currentNode.right, result);
    }

    result.push(currentNode.value);

    return result;
}