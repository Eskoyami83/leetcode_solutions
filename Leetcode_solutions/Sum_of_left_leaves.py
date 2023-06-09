def sumOfLeftLeaves(self, root):
        if root==None or (root.left==None and root.right==None) or root.left==None:
            return 0
        ans=0  
        if root.left.right==None and root.left.left==None:
            ans+=root.left.val
            return ans+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.right)+self.sumOfLeftLeaves(root.left)