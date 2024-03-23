from random import randint
from typing import Callable

from avl_tree import AVLNode, AVLTree


def __apply_binary_func(root: AVLNode, value: int, func: Callable) -> int:
    if root.left:
        value = __apply_binary_func(root.left, value, func)
    if root.right:
        value = __apply_binary_func(root.right, value, func)

    value = func(value, root.key)
    return value


def minimum_node(root: AVLNode) -> int | None:
    if not root:
        return None

    return __apply_binary_func(root, root.key, min)


def maximum_node(root: AVLNode) -> int | None:
    if not root:
        return None

    return __apply_binary_func(root, root.key, max)


def sum_nodes(root: AVLNode) -> int | None:
    if not root:
        return None

    return __apply_binary_func(root, 0, lambda l, r: sum([l, r]))


if __name__ == "__main__":
    root = None
    key_range = 30
    keys = set([randint(-key_range, key_range) for _ in range(key_range)])
    for key in keys:
        root = AVLTree.insert_node(root, key)

    print("AVL-Tree:")
    print(root)

    print("Minimum:", minimum_node(root))
    print("Maximum:", maximum_node(root))
    print("Sum:", sum_nodes(root))
