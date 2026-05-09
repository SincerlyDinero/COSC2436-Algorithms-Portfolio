"""
Lab 08: Balanced Trees
Implement AVL tree from Chapter 8.

Chapter 8 covers:
- BST problems (unbalanced = O(n))
- AVL Trees (self-balancing)
- Splay Trees
- B-Trees
"""
from typing import Optional, Any, List


class AVLNode:
    """AVL tree node with height tracking."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1


class AVLTree:
    """Self-balancing AVL tree."""
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def height(self, node: Optional[AVLNode]) -> int:
        """Return the height of a node (0 if None)."""
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node: Optional[AVLNode]) -> int:
        """Calculate balance factor of a node (left height - right height)."""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, z: AVLNode) -> AVLNode:
        """Perform a right rotation on the subtree rooted at z."""
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights (z first, then y)
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotate_left(self, z: AVLNode) -> AVLNode:
        """Perform a left rotation on the subtree rooted at z."""
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights (z first, then y)
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        """Recursively insert a value and rebalance the subtree."""
        # Standard BST insert
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            # Duplicate values not inserted
            return node

        # Update height of current node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Get balance factor to check if unbalanced
        balance = self.balance_factor(node)

        # Left Left case
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Right Right case
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Left Right case
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left case
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, value: Any) -> None:
        """Insert a value into the AVL tree."""
        self.root = self._insert(self.root, value)

    def _inorder(self, node: Optional[AVLNode], result: List[Any]) -> None:
        """Helper for inorder traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def inorder(self) -> List[Any]:
        """Return inorder traversal of the tree."""
        result: List[Any] = []
        self._inorder(self.root, result)
        return result


if __name__ == '__main__':
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for v in values:
        tree.insert(v)
    print('Inorder traversal:', tree.inorder())
    print('Root:', tree.root.value)
    print('Root height:', tree.root.height)
