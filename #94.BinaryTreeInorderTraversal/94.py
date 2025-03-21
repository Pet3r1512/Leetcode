from typing import List, Optional

import sys
import os

# Add the parent directory (where tree_utils.py is located) to Python’s search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tree_utils import buildTree  # Now import should work

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        def inorder(node: TreeNode):
            if node is None:
                return 
            inorder(node.left)
            r.append(node.val)
            inorder(node.right)
        inorder(root)
        return r

root = buildTree([1, None, 2, 3])

solution_instance = Solution()
print(solution_instance.inorderTraversal(root))
