class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


class AVLTree:
    def __get_height(node):
        if not node:
            return 0
        return node.height

    def __get_balance(node):
        if not node:
            return 0
        return AVLTree.__get_height(node.left) - AVLTree.__get_height(node.right)

    def __left_rotate(z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(AVLTree.__get_height(z.left),
                           AVLTree.__get_height(z.right))
        y.height = 1 + max(AVLTree.__get_height(y.left),
                           AVLTree.__get_height(y.right))

        return y

    def __right_rotate(y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(AVLTree.__get_height(y.left),
                           AVLTree.__get_height(y.right))
        x.height = 1 + max(AVLTree.__get_height(x.left),
                           AVLTree.__get_height(x.right))

        return x

    def __min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert_node(root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = AVLTree.insert_node(root.left, key)
        elif key > root.key:
            root.right = AVLTree.insert_node(root.right, key)
        else:
            return root

        root.height = 1 + max(
            AVLTree.__get_height(root.left), AVLTree.__get_height(root.right)
        )

        balance = AVLTree.__get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return AVLTree.__right_rotate(root)
            else:
                root.left = AVLTree.__left_rotate(root.left)
                return AVLTree.__right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return AVLTree.__left_rotate(root)
            else:
                root.right = AVLTree.__right_rotate(root.right)
                return AVLTree.__left_rotate(root)

        return root

    def delete_node(root, key):
        if not root:
            return root

        if key < root.key:
            root.left = AVLTree.delete_node(root.left, key)
        elif key > root.key:
            root.right = AVLTree.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = AVLTree.__min_value_node(root.right)
            root.key = temp.key
            root.right = AVLTree.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(
            AVLTree.__get_height(root.left), AVLTree.__get_height(root.right)
        )

        balance = AVLTree.__get_balance(root)

        if balance > 1:
            if AVLTree.__get_balance(root.left) >= 0:
                return AVLTree.__right_rotate(root)
            else:
                root.left = AVLTree.__left_rotate(root.left)
                return AVLTree.__right_rotate(root)

        if balance < -1:
            if AVLTree.__get_balance(root.right) <= 0:
                return AVLTree.__left_rotate(root)
            else:
                root.right = AVLTree.__right_rotate(root.right)
                return AVLTree.__left_rotate(root)

        return root


if __name__ == "__main__":
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = AVLTree.insert_node(root, key)
        print("Inserted:", key)

    print("AVL-Tree:")
    print(root)

    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = AVLTree.delete_node(root, key)
        print("Deleted:", key)

    print("AVL-Tree:")
    print(root)
