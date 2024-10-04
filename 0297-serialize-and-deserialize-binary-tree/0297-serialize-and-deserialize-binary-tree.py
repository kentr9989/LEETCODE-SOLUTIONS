# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        
        def dfs(curr):
            if not curr:
                self.res.append("N")
                return 
            self.res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
            
        dfs(root)
        print(self.res)
        return ','.join(self.res)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        print(f"vals: {vals}")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
           
            new_node = TreeNode(int(vals[self.i]))
            self.i += 1
            new_node.left = dfs()
            new_node.right = dfs()
            
            return new_node
        return dfs()
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))