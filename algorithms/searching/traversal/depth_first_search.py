def depth_first_search_pre_order(current_node, result=[]):
    result.append(current_node.value)

    if current_node.left:
        depth_first_search_pre_order(current_node.left, result)
    if current_node.right:
        depth_first_search_pre_order(current_node.right, result)

    return result


def depth_first_search_in_order(current_node, result=[]):
    if current_node.left:
        depth_first_search_in_order(current_node.left, result)

    result.append(current_node.value)

    if current_node.right:
        depth_first_search_in_order(current_node.right, result)

    return result


def depth_first_search_post_order(current_node, result=[]):
    if current_node.left:
        depth_first_search_post_order(current_node.left, result)
    if current_node.right:
        depth_first_search_post_order(current_node.right, result)

    result.append(current_node.value)

    return result
