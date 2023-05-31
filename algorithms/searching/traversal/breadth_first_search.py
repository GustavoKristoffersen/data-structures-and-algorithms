def breadth_first_search(root):
    result = []
    queue = []

    queue.append(root)

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


def breadth_first_search_recursive(queue, result=[]):
    if not queue:
        return result

    current_node = queue.pop(0)
    result.append(current_node.value)
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)

    return breadth_first_search_recursive(queue, result)
