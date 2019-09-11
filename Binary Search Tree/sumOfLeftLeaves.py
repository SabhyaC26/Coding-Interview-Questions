def sumOfLeftLeaves(root):
    if root is None:
        return 0
    leftSum = 0
    queue = [root]
    while queue:
        cur = queue.pop(0)
        if cur.left and not cur.left.left and not cur.left.right:
            leftSum += cur.left.val
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return leftSum
