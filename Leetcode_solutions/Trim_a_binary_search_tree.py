# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def trimBST(self, root, low, high):
	if not root:
		return None
	if root.val>high:
		return self.trimBST(root.left,low, high)
	elif root.val<low:
		return self.trimBST(root.right, low, high)
	root.left=self.trimBST(root.left, low, high)
	root.right=self.trimBST(root.right, low, high)
	return root