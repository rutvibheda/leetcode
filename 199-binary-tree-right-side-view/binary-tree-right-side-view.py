# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        result = []
        
        while q:
            q_length = len(q)  #length of the deque\
            rightSide = None
            
            for i in range(q_length):
                node = q.popleft()
                # rightSide = None
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide: 
                result.append(rightSide.val)
        return result

